import unittest
import pygazebo_ros

import rospy
import roslaunch

import rospkg
import os
import time

test_path = os.path.dirname(os.path.abspath(__file__))
world_path = os.path.join(test_path, 'launch/world_test.world')
gazebo_ros = pygazebo_ros.GazeboROS(world_name=world_path)


class TestGazeboROSServices(unittest.TestCase):

    # -- Getters and setter --
    def test_physics_properties(self):
        gazebo_ros.time_step = 0.002
        time_step = gazebo_ros.time_step
        self.assertEqual(time_step, 0.002)
        gazebo_ros.time_step = 0.005
        time_step = gazebo_ros.time_step
        self.assertEqual(time_step, 0.005)

        gazebo_ros.max_update_rate = 500
        max_update_rate = gazebo_ros.max_update_rate
        self.assertEqual(max_update_rate, 500)
        gazebo_ros.max_update_rate = 1000
        max_update_rate = gazebo_ros.max_update_rate
        self.assertEqual(max_update_rate, 1000)

        gazebo_ros.gravity = [1.0, 1.0, -1.0]
        gravity = gazebo_ros.gravity
        self.assertEqual(gravity, [1.0, 1.0, -1.0])
        gazebo_ros.gravity = [0.0, 0.0, -9.8]
        gravity = gazebo_ros.gravity
        self.assertEqual(gravity, [0.0, 0.0, -9.8])

        # FIXME: with can't I set auto_disable_bodies ????
        # gazebo_ros.auto_disable_bodies = True
        # auto_disable_bodies = gazebo_ros.auto_disable_bodies
        # self.assertTrue(auto_disable_bodies)
        # gazebo_ros.auto_disable_bodies = False
        # auto_disable_bodies = gazebo_ros.auto_disable_bodies
        # self.assertFalse(auto_disable_bodies)

        gazebo_ros.sor_pgs_precon_iters = 10
        sor_pgs_precon_iters = gazebo_ros.sor_pgs_precon_iters
        self.assertEqual(sor_pgs_precon_iters, 10)
        gazebo_ros.sor_pgs_precon_iters = 0
        sor_pgs_precon_iters = gazebo_ros.sor_pgs_precon_iters
        self.assertEqual(sor_pgs_precon_iters, 0)

        gazebo_ros.sor_pgs_iters = 51
        sor_pgs_iters = gazebo_ros.sor_pgs_iters
        self.assertEqual(sor_pgs_iters, 51)
        gazebo_ros.sor_pgs_iters = 50
        sor_pgs_iters = gazebo_ros.sor_pgs_iters
        self.assertEqual(sor_pgs_iters, 50)

        gazebo_ros.sor_pgs_w = 1.4
        sor_pgs_w = gazebo_ros.sor_pgs_w
        self.assertEqual(sor_pgs_w, 1.4)
        gazebo_ros.sor_pgs_w = 1.3
        sor_pgs_w = gazebo_ros.sor_pgs_w
        self.assertEqual(sor_pgs_w, 1.3)

        # FIXME: why can't I change sor_pgs_rms_error_tol ??
        # gazebo_ros.sor_pgs_rms_error_tol = 0.1
        # sor_pgs_rms_error_tol = gazebo_ros.sor_pgs_rms_error_tol
        # self.assertEqual(sor_pgs_rms_error_tol, 0.1)
        # gazebo_ros.sor_pgs_rms_error_tol = 0
        # sor_pgs_rms_error_tol = gazebo_ros.sor_pgs_rms_error_tol
        # self.assertEqual(sor_pgs_rms_error_tol, 0)

        gazebo_ros.contact_surface_layer = 0.002
        contact_surface_layer = gazebo_ros.contact_surface_layer
        self.assertEqual(contact_surface_layer, 0.002)
        gazebo_ros.contact_surface_layer = 0.001
        contact_surface_layer = gazebo_ros.contact_surface_layer
        self.assertEqual(contact_surface_layer, 0.001)

        gazebo_ros.contact_max_correcting_vel = 200
        contact_max_correcting_vel = gazebo_ros.contact_max_correcting_vel
        self.assertEqual(contact_max_correcting_vel, 200)
        gazebo_ros.contact_max_correcting_vel = 100
        contact_max_correcting_vel = gazebo_ros.contact_max_correcting_vel
        self.assertEqual(contact_max_correcting_vel, 100)

        gazebo_ros.cfm = 0.1
        cfm = gazebo_ros.cfm
        self.assertEqual(cfm, 0.1)
        gazebo_ros.cfm = 0.0
        cfm = gazebo_ros.cfm
        self.assertEqual(cfm, 0.0)

        gazebo_ros.erp = 0.3
        erp = gazebo_ros.erp
        self.assertEqual(erp, 0.3)
        gazebo_ros.erp = 0.2
        erp = gazebo_ros.erp
        self.assertEqual(erp, 0.2)

        gazebo_ros.max_contacts = 30
        max_contacts = gazebo_ros.max_contacts
        self.assertEqual(max_contacts, 30)
        gazebo_ros.max_contacts = 20
        max_contacts = gazebo_ros.max_contacts
        self.assertEqual(max_contacts, 20)

    # -- Service methods --
    # region
    def test_apply_body_wrench(self):
        gazebo_ros.apply_body_wrench(
            body_name='model_test_1::link_1',
            reference_frame='',
            reference_point=[1, 1, 1],
            force=[1, 0, 2],
            torque=[0, 2, 1],
            start_time_secs=0,
            start_time_nsecs=8000,
            duration_secs=15,
            duration_nsecs=1564)

    def test_apply_joint_effort(self):
        gazebo_ros.apply_joint_effort(
            joint_name='model_test_1::joint',
            effort=1,
            start_time_secs=2,
            start_time_nsecs=58,
            duration_secs=3,
            duration_nsecs=7)

    def test_clear_body_wrenches(self):
        gazebo_ros.clear_body_wrenches(
            body_name='model_test_1::link_1')

    def test_clear_joint_forces(self):
        gazebo_ros.clear_joint_forces(
            joint_name='model_test_1::joint')

    def test_delete_light(self):
        gazebo_ros.delete_light(
            light_name='light_test_1')

    def test_delete_model(self):
        gazebo_ros.delete_model(
            model_name='model_test_2')

    def test_get_joint_properties(self):
        gazebo_ros.get_joint_properties(
            joint_name='model_test_1::joint')

    def test_get_light_properties(self):
        self.assertIsInstance(gazebo_ros.get_light_properties(
            light_name='light_test_2'), dict)

    def test_get_link_properties(self):
        self.assertIsInstance(gazebo_ros.get_link_state(
            link_name='model_test_1::link_1'), dict)

    def test_get_link_state(self):
        self.assertIsInstance(gazebo_ros.get_link_state(
            link_name='model_test_1::link_1'), dict)

    def test_get_loggers(self):
        self.assertIsInstance(
            gazebo_ros.get_loggers(), dict)

    def test_get_model_properties(self):
        self.assertIsInstance(
            gazebo_ros.get_model_properties(
                model_name='model_test_1'), dict)

    def test_get_model_state(self):
        self.assertIsInstance(
            gazebo_ros.get_model_state(
                model_name='model_test_1', relative_entity_name=''), dict)

    def test_get_physics_properties(self):
        self.assertIsInstance(
            gazebo_ros.get_physics_properties(), dict)

    def test_get_world_properties(self):
        self.assertIsInstance(
            gazebo_ros.get_world_properties(), dict)

    def test_pause_physics(self):
        gazebo_ros.pause_physics()
        self.assertTrue(gazebo_ros.paused)

    def test_reset_simulation(self):
        gazebo_ros.reset_simulation()

    def test_reset_world(self):
        gazebo_ros.reset_world()

    def test_set_joint_properties(self):
        gazebo_ros.set_joint_properties(
            joint_name='model_test_1::joint',
            damping=[0.1],
            hiStop=[100],
            loStop=[-100],
            erp=[0.3],
            cfm=[0.0001],
            stop_erp=[0.6],
            stop_cfm=[0.0001],
            fudge_factor=[1.0],
            fmax=[10],
            vel=[0.01])

    def test_set_light_properties(self):
        gazebo_ros.set_light_properties(
            light_name='light_test_2',
            diffuse=[0.5, 0.5, 0.5, 1.0],
            attenuation_constant=0.9,
            attenuation_linear=0.3,
            attenuation_quadratic=0.01)

    def test_set_link_properties(self):
        gazebo_ros.set_link_properties(
            link_name='model_test_1::link_1',
            position=[5.0, 5.0, 10.0],
            orientation=[0.2, 0.5, 0.8, 0.4],
            gravity_mode=False,
            mass=4,
            ixx=1.0,
            ixy=0.0,
            ixz=0.0,
            iyy=1.0,
            iyz=0.0,
            izz=1.0)

    def test_set_link_state(self):
        gazebo_ros.set_link_state(
            link_name='model_test_3::link',
            position=[5.0, 6.0, 10.0],
            orientation=[0.2, 0.6, 0.8, 0.4],
            linear_velocity=[0.0, 0.0, 0.1],
            angular_velocity=[0.1, 0.0, 0.0],
            reference_frame='')
        ls = gazebo_ros.get_link_state(link_name='model_test_3::link')
        self.assertAlmostEqual(ls['position'][0], 5.0, places=1)

    def test_set_logger_level(self):
        gazebo_ros.set_logger_level(logger='ros.roscpp', level='warn')
        loggers = gazebo_ros.get_loggers()
        self.assertEqual(loggers['ros.roscpp']['level'], 'warn')

    def test_set_model_configuration(self):
        gazebo_ros.set_model_configuration(
            model_name='model_test_1',
            urdf_param_name='',
            joint_names=['joint'], joint_positions=[2.0])
        joint_position = gazebo_ros.get_joint_properties(
            'model_test_1::joint')['position'][0]
        self.assertAlmostEqual(joint_position, 2.0, places=2)

    def test_set_model_state(self):
        desired_pos = [4.0, 9.0, 3.0]
        gazebo_ros.set_model_state(
            model_name='model_test_1',
            position=desired_pos,
            orientation=[4, 5, 6, 7],
            linear_velocity=[0.1, 0.1, -0.1],
            angular_velocity=[0.1, 0.2, -0.2],
            reference_frame='')
        pos = gazebo_ros.get_model_state(
            model_name='model_test_1',
            relative_entity_name='')['position']
        for i in range(3):
            self.assertAlmostEqual(desired_pos[i], pos[i], places=1)

    def test_set_parameters(self):
        out = gazebo_ros.set_parameters(
            bools=[],
            ints=[],
            strs=[],
            doubles=[{'name': 'gravity_x', 'value': 0.1}],
            groups=[])
        for item in out['doubles']:
            if item['name'] == 'gravity_x':
                self.assertEqual(item['value'], 0.1)

    def test_set_physics_properties(self):
        gazebo_ros.set_physics_properties(
            time_step=0.001,
            max_update_rate=1000.0,
            gravity=[0.1, 0.2, -9.8],
            auto_disable_bodies=False,
            sor_pgs_precon_iters=0,
            sor_pgs_iters=50,
            sor_pgs_w=1.4,
            sor_pgs_rms_error_tol=0.0,
            contact_surface_layer=0.0,
            contact_max_correcting_vel=0.0,
            cfm=0.0,
            erp=1.0,
            max_contacts=20)
        self.assertEqual(gazebo_ros.gravity[1], 0.2)

    def test_spawn_sdf_model(self):
        model_xml = '''<?xml version="1.0" ?>
            <sdf version="1.5">
                <model name="unused_name">
                    <link name="link">
                    <collision name="collision">
                        <pose>0 0 0.5 0 0 0</pose>
                        <geometry>
                        <box>
                            <size>1 1 1</size>
                        </box>
                        </geometry>
                    </collision>
                    <visual name="collision">
                        <pose>0 0 0.5 0 0 0</pose>
                        <geometry>
                        <box>
                            <size>1 1 1</size>
                        </box>
                        </geometry>
                    </visual>
                    </link>
                </model>
            </sdf>'''
        gazebo_ros.spawn_sdf_model(
            model_name='test_model_sdf',
            model_xml=model_xml,
            robot_namespace='test_robot_namespace_sdf',
            initial_position=[-2.0, 3.0, 5.0],
            initial_orientation=[0.1, 0.1, 0.2, 0],
            reference_frame='')

    def test_spawn_urdf_model(self):
        model_xml = '''<?xml version="1.0"?>
            <robot name="robot">
                <link name="base_link">
                    <collision>
                        <origin xyz="0 0 1" rpy="0 0 0"/>
                        <geometry>
                            <box size="2 2 2"/>
                        </geometry>
                    </collision>
                    <visual>
                        <origin xyz="0 0 1" rpy="0 0 0"/>
                        <geometry>
                            <box size="2 2 2"/>
                        </geometry>
                    </visual>
                    <inertial>
                        <origin xyz="0 0 0" rpy="0 0 0"/>
                        <mass value="1"/>
                        <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="1.0" iyz="0.0" izz="1.0"/>
                    </inertial>
                </link>
            </robot>'''
        gazebo_ros.spawn_urdf_model(
            model_name='test_model_urdf',
            model_xml=model_xml,
            robot_namespace='test_robot_namespace_urdf',
            initial_position=[0, 0, 10],
            initial_orientation=[0, 0.1, 0.2, 0],
            reference_frame='')

    def test_unpause_physics(self):
        gazebo_ros.unpause_physics()
        self.assertFalse(gazebo_ros.paused)

    # endregion

    # -- Derived method --
    # region
    def test_apply_body_force(self):
        gazebo_ros.apply_body_force(
            body_name='model_test_4::link',
            reference_point=[0, 0, 0],
            force=[0, 0.1, 0.1],
            start_time=1.000001,
            reference_frame='model_test_4::link')

    def test_apply_body_torque(self):
        gazebo_ros.apply_body_torque(
            body_name='model_test_4::link',
            torque=[0.1, 0.2, 0.3],
            start_time=2.000001,
            reference_frame='model_test_4::link')

    def test_get_sim_time(self):
        self.assertIsInstance(gazebo_ros.get_sim_time(), float)

    def test_spawn_light(self):
        gazebo_ros.spawn_light(
            light_name='testing_light',
            position=[1.0, 2.0, 3.0],
            yaw=0.1, pitch=0.2, roll=-0.9,
            diffuse_red=0.9, diffuse_green=0.8, diffuse_blue=0.7, diffuse_alpha=0.6,
            specular_red=0.5, specular_green=0.4, specular_blue=0.3, specular_alpha=0.2,
            attenuation_range=10,
            attenuation_constant=0.55,
            attenuation_linear=0.4,
            attenuation_quadratic=0.3,
            cast_shadows=True)
        attenuation_constant = gazebo_ros.get_light_properties(
            light_name='testing_light')['attenuation_constant']
        self.assertAlmostEqual(attenuation_constant, 0.55)

    # endregion

    # -- Miscellaneous --
    # region

    def test_pausing_context(self):
        with gazebo_ros.pausing():
            self.assertTrue(gazebo_ros.paused)
            time.sleep(1)
        self.assertFalse(gazebo_ros.paused)
    # endregion