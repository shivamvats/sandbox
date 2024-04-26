from Box2D import b2
import pygame
import numpy as np


class ShelfEnv:
    """Single pusher is to be used to push objs to the goal region.
    * Out of plane motion is allowed.
    """

    SCREEN_WIDTH, SCREEN_HEIGHT = 700, 700
    PPM = 600.0

    def __init__(self, env_cfg, gui=True):
        # sim params
        self.TARGET_FPS = 20
        self.TIMESTEP = 1.0 / self.TARGET_FPS
        self._vel_iters, self._pos_iters = 10, 10

        # env
        self._xmax = 3
        self._ymax = 3
        self._cfg = env_cfg

        self._obj_pose_names = ["shelf/pose", "box/pose"]
        self._obj_vel_names = ["shelf/vel", "box/vel"]

        self._world = b2.world(gravity=(0.0, 0.0))

        self._shelf_color = [127, 127, 255]
        self._box_color = [127, 255, 127]

        # TODO Add boundary
        # self._ground = self._world.CreateStaticBody(
        # position=(0, -0.05),
        # shapes=b2.polygonShape(box=(1, 0.1))
        # )

        # Insert Bodies
        self._bodies = []
        body = self._world.CreateDynamicBody(
            position=(1, 1), linearDamping=0.5, angularDamping=0.5
        )
        _ = body.CreatePolygonFixture(
            box=(0.1, 0.125),
            density=200,
            friction=0.2,
        )
        self._bodies.append(body)

        # Insert Pusher
        # shelf = world.CreateStaticBody(
            # position=(0, 0),
            # shapes=polygonShape(box=(50, 1)),
        # )

        if gui:
            self._screen = pygame.display.set_mode(
                (self.SCREEN_WIDTH, self.SCREEN_HEIGHT), 0, 32
            )
            pygame.display.set_caption("Object Sorting")
            self._clock = pygame.time.Clock()
            self._screen.fill((100, 100, 100))

        #  TODO: make note of transform.R.set() -> transform.angle =
        # xf1 = b2Transform()
        # xf1.angle = 0.3524 * b2_pi
        # xf1.position = xf1.R * (1.0, 0.0)

        # xf2 = b2Transform()
        # xf2.angle = -0.3524 * b2_pi
        # xf2.position = xf2.R * (-1.0, 0.0)
        # self.body = self.world.CreateDynamicBody(
        # position=(0, 2),
        # angle=b2_pi,
        # angularDamping=5,
        # linearDamping=0.1,
        # shapes=[b2PolygonShape(vertices=[xf1 * (-1, 0), xf1 * (1, 0),
        # xf1 * (0, .5)]),
        # b2PolygonShape(vertices=[xf2 * (-1, 0), xf2 * (1, 0),
        # xf2 * (0, .5)])],
        # shapeFixture=b2FixtureDef(density=2.0),
        # )

        # gravity = 10.0
        # fixtures = b2FixtureDef(shape=b2PolygonShape(box=(0.5, 0.5)),
        # density=1, friction=0.3)
        # for i in range(10):
        # body = self.world.CreateDynamicBody(
        # position=(0, 5 + 1.54 * i), fixtures=fixtures)

        # # For a circle: I = 0.5 * m * r * r ==> r = sqrt(2 * I / m)
        # r = sqrt(2.0 * body.inertia / body.mass)

        # self.world.CreateFrictionJoint(
        # bodyA=ground,
        # bodyB=body,
        # localAnchorA=(0, 0),
        # localAnchorB=(0, 0),
        # collideConnected=True,
        # maxForce=body.mass * gravity,
        # maxTorque=body.mass * r * gravity
        # )

    def step(self, action):
        """Each action consists of a pushing direction and force."""
        # apply action
        # self._pusher.SetLinearVelocity
        # self._pusher.ApplyForceToCenter([action.dx, action.dy], True)

        self._world.Step(self.TIMESTEP, self._vel_iters, self._pos_iters)
        self._draw()
        pygame.display.flip()
        self._clock.tick(self.TARGET_FPS)
        self._world.ClearForces()
        print(self._bodies[0].position, self._bodies[0].linearVelocity)

    def destroy(self):
        pygame.quit()

    @property
    def state(self):
        """Returns a dictionary containing the state of every movable object."""
        state = State()

        # objs
        for body, pose_name, vel_name in zip(
            self._bodies, self._obj_pose_names, self._obj_vel_names
        ):
            state.update_property(
                pose_name, [body.position.x, body.position.y, body.angle]
            )
            state.update_property(
                vel_name,
                [body.linearVelocity.x, body.linearVelocity.y, body.angularVelocity],
            )

        # pusher
        # body = self._pusher
        # state.update_property(
            # "pusher0/pose", [body.position.x, body.position.y, body.angle]
        # )
        # state.update_property(
            # f"pusher0/vel",
            # [body.linearVelocity.x, body.linearVelocity.y, body.angularVelocity],
        # )
        return state

    @state.setter
    def state(self, new_state):
        new_poses = self._get_object_poses(new_state)
        new_vels = self._get_object_vels(new_state)
        for body, pose, vel in zip(self._bodies, new_poses, new_vels):
            body.position.x = pose[0]
            body.position.y = pose[1]
            body.angle = pose[2]
            body.linearVelocity.x = vel[0]
            body.linearVelocity.y = vel[1]
            body.angularVelocity = vel[2]

    def _draw(self):
        self._screen.fill((100, 100, 100))
        for body in self._bodies:
            for fixture in body.fixtures:
                shape = fixture.shape
                vertices = [(body.transform * v) * self.PPM for v in shape.vertices]
                vertices = [(v[0], self.SCREEN_HEIGHT - v[1]) for v in vertices]
                pygame.draw.polygon(self._screen, self._box_color, vertices, 0)
                # int(radius*self.PPM), 0)

        # body = self._pusher
        # for fixture in body.fixtures:
            # shape = fixture.shape
            # vertices = [(body.transform * v) * self.PPM for v in shape.vertices]
            # vertices = [(v[0], self.SCREEN_HEIGHT - v[1]) for v in vertices]
            # pygame.draw.polygon(self._screen, self._pusher_color, vertices, 0)

    def _get_object_poses(self, state):
        poses = np.array(
            state.get_values_as_vec(
                self._obj_pose_names,
            )
        ).reshape(-1, 3)
        return poses

    def _get_object_vels(self, state):
        vels = np.array(
            state.get_values_as_vec(
                self._obj_vel_names,
            )
        ).reshape(-1, 3)
        return vels

    def _get_object_sizes(self, state):
        sizes = np.array(
            state.get_values_as_vec(
                self._obj_size_names,
            )
        ).reshape(-1, 3)
        return sizes


def main():
    env = ShelfEnv({}, gui=True)
    for i in range(1000):
        # plan = planner.replan()
        # print(plan)
        env.step(0)
    env.destroy()

if __name__ == "__main__":
    main()
