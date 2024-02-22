from array import array
from this import d
from pkg_resources import ContextualVersionConflict
import pygame, pymunk, math, partical_obj

####controls 
#click to place
#w/s to increace/decreace side length
#a to swap active sides
#r to rotate
#d to toggle physics **recomended for precise building**
#q to toggle between blocks and circles
#(you may have to swap active sides to scale circles)


w, h = 1250, 800

def convert_cords(point):
    return point[0], h-point[1]


clock = pygame.time.Clock()

win = pygame.display.set_mode((w, h))

main_s = pygame.surface.Surface((w, h))

main_s.set_colorkey((0, 0, 0))

space = pymunk.Space()

space.gravity = 0, -100

pin_pos1 = (0, 0)

#add floor to physics
seg_body = pymunk.Body(body_type=pymunk.Body.STATIC)
floor_pos = [(0,h - h/10 - 1), (w, h - h/10 - 1)]
seg_shape = pymunk.Segment(seg_body, convert_cords(floor_pos[0]), convert_cords(floor_pos[1]), 9)
seg_shape.mass = 10
seg_shape.friction = 5
space.add(seg_body, seg_shape)

particals = []
selected_objs = []
joints = []


def toggle(bool_var):
    if bool_var:
        return False
    else:
        return True



def main_loop():

    h_mod, w_mod = 10,10
    #col id >= 5 are for objects, under 5 is special colision states
    col_id = 5

    run = True

    disable_physics = False

    rotate = False
    
    side_mode = True

    is_circle = False

    select_mode = False

    pin_mode = False

    static_bool = False

    fps = 60

    #outline for objects before placement
    preview_box = pygame.Surface((10, 10))


    cursor = partical_obj.Partical(False, 0, 0, 2, pymunk.Body.KINEMATIC, True)
    cursor_active = True
    fifo_bool = False
    selected_angle = 0

    scaling_mult = 1

    


    while run:

        clock.tick(fps)

        main_s.fill((255, 255, 255))

        space.step(1/(fps * 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if select_mode:
                    #on mouse click spawn a circle wiht colision type 1 at mouse position
                    if cursor_active:
                        cursor.body.position = convert_cords(pygame.mouse.get_pos())
                        cursor.shape.collision_type = 1
                        if not fifo_bool:
                            space.add(cursor.body, cursor.shape)
                            fifo_bool = True
                        
                    else:
                        
                        for obj in particals:
                            if obj.shape.collision_type == 2:
                                
                                x, y = pygame.mouse.get_pos()
                                x = int(x/5) * 5
                                y = int(y/5) * 5
                                obj.body.position = convert_cords((x, y))
                                obj.deselected()
                                cursor.shape.collision_type = 2
                                cursor_active = True
                                break
                elif pin_mode:
                    if cursor_active:
                        cursor.body.position = convert_cords(pygame.mouse.get_pos())
                        pin_pos1 = pygame.mouse.get_pos()
                        cursor.shape.collision_type = 4
                        if not fifo_bool:
                            space.add(cursor.body, cursor.shape)
                            fifo_bool = True
                        
                    else:
                        
                        for obj in particals:
                            if obj.shape.collision_type == 2:
                                
                                x, y = pygame.mouse.get_pos()
                                x = int(x/5) * 5
                                y = int(y/5) * 5
                                obj.body.position = convert_cords((x, y))
                                obj.deselected()
                                cursor.shape.collision_type = 2
                                cursor_active = True
                                break
                    
                else:
                    if fifo_bool:
                        space.remove(cursor.body, cursor.shape)
                        fifo_bool = False

                    #on mouse press make new partical object

                    x, y = pygame.mouse.get_pos()
                    
                    #snap position to the nearest 5th position 
                    #produces grid effect
                    x = int(x/5) * 5
                    y = int(y/5) * 5

                    if static_bool:
                        type = pymunk.Body.STATIC
                    else:
                        type = pymunk.Body.DYNAMIC

                    new_partical = partical_obj.Partical(rotate, w_mod, h_mod, col_id,type, is_circle)
                    
                    handeler = space.add_collision_handler(col_id, 1)
                    handeler.begin = new_partical.selected

                    handeler = space.add_collision_handler(col_id, 2)
                    handeler.begin = new_partical.disable_col

                    handeler = space.add_collision_handler(col_id, 4)
                    handeler.begin = new_partical.pin_selected
                    col_id += 1

                    body = new_partical.body
                    body.position = convert_cords((x,y))

                    shape = new_partical.shape

                    space.add(body, shape)

                    particals.append(new_partical)

                
                
            if event.type == pygame.KEYDOWN and not select_mode:
                #key functions

                if event.key == pygame.K_d:
                    #toggle physics
                    disable_physics = toggle(disable_physics)
                    if not disable_physics:
                        space.gravity = (0, -100)

                if event.key == pygame.K_r:
                    #rotate object
                    rotate = toggle(rotate)

                if event.key == pygame.K_w:
                    #increase sellected side length
                    if side_mode and w_mod >= 0:
                        w_mod += 5 * scaling_mult
                    elif h_mod >= 0:
                        h_mod += 5 * scaling_mult

                if event.key == pygame.K_s:
                    #decrease selected side length
                    if side_mode and w_mod - 5 * select_mode > 0:
                        w_mod -= 5 * scaling_mult
                    elif h_mod - 5 * scaling_mult >= 0:
                        h_mod -= 5 * scaling_mult
                    else:
                        h_mod = 5
                        w_mod = 5

                if event.key == pygame.K_a:
                    #change side mode
                    side_mode = toggle(side_mode)

                if event.key == pygame.K_q:
                    #change to circle mode
                    is_circle = toggle(is_circle)
                
                if event.key == pygame.K_e:
                    #toggle select mode
                    select_mode = toggle(select_mode)

                if event.key == pygame.K_f:
                    pin_mode = toggle(pin_mode)

                if event.key == pygame.K_1 and scaling_mult > 1:
                    scaling_mult -= 1
                    
                
                if event.key == pygame.K_2:
                    scaling_mult += 1

                if event.key == pygame.K_c:
                    static_bool = toggle(static_bool)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    #toggle select mode
                    select_mode = toggle(select_mode)

                if event.key == pygame.K_w:
                    if not selected_angle >= 360 - (5 * (scaling_mult)):
                        selected_angle += 5 * select_mode
                    else:
                        selected_angle = 0

                if event.key == pygame.K_s: 
                    if selected_angle ==0:
                        selected_angle = 360 - 5 * scaling_mult
                    else:
                        selected_angle -= 5 * scaling_mult
                
                if event.key == pygame.K_1 and scaling_mult > 1:
                    scaling_mult -= 1
                    
                
                if event.key == pygame.K_2:
                    scaling_mult += 1
                
                if event.key == pygame.K_d:
                    
                    for obj in selected_objs:
                        obj.shape.collision_type = 3


        cursor.body.position = convert_cords(pygame.mouse.get_pos())
                       
        for j in joints:
            pv1 = j.a.position - (j.a.position - j.anchor_a)
            pv2 = j.b.position - (j.b.position - j.anchor_b)
            pygame.draw.line(main_s, (1, 1, 1), convert_cords(pv1), convert_cords(pv2), 5)


        for part in particals:
            #updating and drawing all the objects

            if select_mode and part.is_selected:

                
                if part not in selected_objs:
                    selected_objs.append(part)
                else:
                    part.body.angle = math.radians(selected_angle)
                    part.body.angular_velocity = 0
                    part.body.velocity = (0,0)

                
                        
                    x, y = pygame.mouse.get_pos()
                    x = int(x/5) * 5
                    y = int(y/5) * 5

                    cords = x, y
                    part.body.position = convert_cords(cords)
                    if cursor_active and not part.shape.collision_type == 3:
                        cursor.shape.collision_type = 2
                        cursor_active = False
                        if fifo_bool:
                            space.remove(cursor.body, cursor.shape)
                            fifo_bool = False
                    
                    if part.shape.collision_type == 3:
                            selected_objs.remove(part)
                            space.remove(part.body, part.shape)
                            particals.remove(part)
                            cursor_active = True
                            cursor.shape.collision_type = 2
                            fifo_bool = False
                                    
                
                    
            elif pin_mode:
                if part.shape.collision_type == 3 and not part in selected_objs:
                    selected_objs.append(part)
                    cursor_active = True
                    cursor.shape.collision_type = 2
                    if fifo_bool:
                        space.remove(cursor.body, cursor.shape)
                        fifo_bool = False
                num = 0
                for x in selected_objs:
                    num += 1
                if num >= 2:
                    if part.pinning:
                        part1 = selected_objs[0]
                        part2 = selected_objs[1]
                        joint = pymunk.constraints.PinJoint(part1.body, part2.body, pin_pos1, pygame.mouse.get_pos())
                        
                        joints.append(joint)

                        joint.activate_bodies()

                        joint.error_bias = 0.04
                        
                        space.add(joint)
                        selected_objs.remove(part1)
                        selected_objs.remove(part2)
                        part1.shape.collision_type = part1.col_id
                        part2.shape.collision_type = part2.col_id
                        
                
                cords = convert_cords(part.body.position)
            else:
                if part in selected_objs and not part.is_selected:
                        selected_objs.remove(part)

                cords = convert_cords(part.body.position)
                
            
            
            part.update(cords)

            if disable_physics:
                part.body.velocity = (0, 0)
                part.body.angular_velocity = 0
                space.gravity = (0, 0)

            main_s.blit(part.image, part.rect)

        

        
        #logic for shaping the preview box
        if not is_circle:
            #makes box match witdth height and rotation
            preview_box.set_colorkey((255, 255, 255))
            if rotate:
                preview_box = pygame.transform.scale(preview_box, (5 + h_mod, 5 + w_mod))
            else:
                preview_box = pygame.transform.scale(preview_box, (5 + w_mod, 5 + h_mod))

            preview_box.fill(pygame.Color('black'))
        else:
            #makes box into outline of circle 
            preview_box.set_colorkey((0, 0, 0))
            preview_box.fill((1, 1, 1, 0))
            preview_box = pygame.transform.scale(preview_box, (5 + h_mod, 5 + h_mod))
            pygame.draw.circle(preview_box ,(0, 0, 0) ,(((5 + h_mod) // 2, (5 + h_mod) // 2)), (5 + h_mod)//2)

        
        #snaps preview box to grid
        x, y = pygame.mouse.get_pos()
        x = int(x/5) * 5
        y = int(y/5) * 5
        
        #draws floor
        pygame.draw.line(main_s, (0, 0, 0), floor_pos[0], floor_pos[1], 20)
        
        
        #center at mouse position
        pre_rect = preview_box.get_rect(center = (x, y) )
         
        #draw all to display
        win.blit(main_s, (0,0))
        if not select_mode and not pin_mode:
            win.blit(preview_box, pre_rect )
       
        

        pygame.display.update()
    
    pygame.quit()


main_loop()

