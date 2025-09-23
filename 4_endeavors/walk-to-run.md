---
tags:
  - endeavors/research
status: todo
---

# Humanoid

- how can we transfer learning to walk at low speeds to running
- general image dynamics
- can we encode poses in scenes in the fourier space
- use oscillators to clean our skating pose

- there are two legged robots 

[see this paper](https://leggedrobotics.github.io/identifying_terrain_physical_parameters_webpage/)

## Training Pipeline

- `run_hydra.py`:
    - processes args, calls
    - calls `Runner.{load, reset, run}()`

- `Runner.run()` calls `run_train()` if `args['train']`

- `Runner.run_train()`
    - `agent = algo_factory.create(self.algo_name)` which calls `AMPAgent.__init__`
    - `agent.train()`
# Agents

## init

- `IMAmpAgent(AMPAgent(CommonAgent (A2CAgent(ContinuousA2CBase(A2CBase)))))`
    - note:
        - for some reason `CommonAgent` inherits from `A2CAgent` but in its' `init` function, it calls `A2CBase.__init__`
        - this is likely done to skip some things that are being done in `A2CAgent` or `ContinuousA2CBase`'s `init`s
    - `__init__`:
        - `CommonAgent.__init__`:
            - `A2CBase.__init__`:
                - sets fieldsn
                - `self.vec_env: RLGPUEnv = vecenv.create_vec_env` 
            - sets fields
        -  sets fields

## train

- `IMAmpAgent(AMPAgent(CommonAgent(...)))`:
    - `train() -> CommonAgent.train`
        - loop
            - `epoch_num = A2CAgent.update_epoch()` just increments `self.epoch_num`
            - `train_info = AMPAgent.train_epoch()`:
                - `AMPAgent.pre_epoch()`: 
                    - `HumanoidImGetup.resample_motions()`
                        - `HumanoidAMP.resample_motions()`
                            - `self._motion_lib.load_motions()`
                        - if not testing: `HumanoidImGetup._generate_fall_states()`
                    - if `Humanoid.getup_schedule` is `True`: `HumanoidIMGetup.update_getup_schedule`
                    - `running_mean_std_temp = deepcopy(self.running_mean_std)`
                        - actor should no use updated `running_mean_std`
                - `batch_dict = AMPAgent.play_steps()` (no grad)
                    - `A2CBase.experience_buffer: rl_games.common.experience.ExperienceBuffer` rollout
                    - for loop `self.horizon_length`
                        - reset `AMPAgent.env_reset(done_indices)`
                        - get actions with `res_dict = get_action_values`
                        - fills up `ExperienceBuffer` which is wrapper around a `dict` of tensors with shape: `(horizon_length, num_agents * num_actors, VAL_SHAPE)
                    - then returns the tensor dict with vals reshaped to `(num_agents * num_actors * horizon_length, VAL_SHAPE)` notice axis swap before reshape
                - `AMPAgent.prepare_dataset(batch_dict)`: sets `self.dataset`
                - for loop `mini_epochs_num`:
                    - for `self.dataset`: 
                        - `A2CAgent.train_actor_critic(ds[i])`:
                            - `curr_train_info = AMPAgent.calc_gradients()`
                            - compiles `curr_train_info` into `train_info`
                - `AMPAgent.post_epoch()`: 
                    - `running_mean_std_temp` stuff
                - returns `train_info`
            - return after `max_epochs` reached
# Envs

## init

- `HumanoidAMP(Humanoid(BaseTask)).__init__()`: 
    - `Humanoid(BaseTask).__init__()`
        - `BaseTask.__init__()`
            - `self.gym = gymapi.acquire_gym()`
            - sets:
                - `num_envs = 3072`
                - `num_observations = 934` ??
                - `num_states = 0`??
                - `num_actions = 69`
                - `control_freq_inv = 2`?
            - `Humanoid.create_sim()`
                - `BaseTask.create_sim()`
                - `Humanoid._create_envs()`
                    - `robot = smpl_lib.SMPL_Robot.__init__()`
                        - `smpl_parser_{n,m,f} = SMPL_Parser()`
                        - `self.load_from_skeleton()`
                        - `self._load_motion()`

    - `HumanoidAMP._load_motion()`
        - `self._motion_lib = MotionLibSMPL(MotionLibBase).__init__()`
            - `MotionLibBase.__init__()`
                - `MotionLibBase.load_data()`: first motion load
            - `smpl_parser_{n,m,f} = SMPL_Parser()`
        - `self._motion_lib.load_motions()`


- `SMPL_Parser` from `smpl_lib`, a wrapper around `SMPL(nn.Module)`

- `SMPL(nn.Module)` from `smplx.body_models`

- `RLGPUEnv(vecenv.IVecEnv)`: essentially a wrapper around the env defined in `cfg["task"]`
    - `__init__`:
        - `self.env: HumanoidIm[Getup] = rl_games.common.env_configurations(.)`

### Step

- `BaseTask.step()`
    - `Humanoid.pre_physics_step`
        - `pd_tar = self.action_to_pd_targets(actions)`
            - `return self._pd_action_offset + self._pd_action_scale * action`
    
    - `Humanoid._physics_step`
        - `Humanoid.render`
            - `BaseTask.render`
        - if `self.control_mode == "pd"`
            - `self.torques = self._compute_torques`
            - `self.gym.set_dof_actuation_force_tensor(sim, torques)`
        - `self.gym.simulate(self.sim)`
        
    - `Humanoid.post_physics_step`
        - `Humanoid._update_tensor_history`
            - keeps track of pos, rot, vel, ang vel values
            - WHY?
        - `Humanoid._refresh_sim_tensor`:
            - self.gym.refresh_dof_state_tensor(self.sim)
            - self.gym.refresh_actor_root_state_tensor(self.sim)
            - self.gym.refresh_rigid_body_state_tensor(self.sim)
            - `ADDITIONAL LOGIC`
            - self.gym.refresh_force_sensor_tensor(self.sim)
            - self.gym.refresh_dof_force_tensor(self.sim)
            - self.gym.refresh_net_contact_force_tensor(self.sim)
        - `Humanoid._update_tensor_history`
        - 

## Questions

- todo: figure out shape of specific tensors and their meaning:
    - `agent.dataset`, values_dict
    - `self.obs` in each loop of `play_steps`
    - `res_dict` in each loop of `play_steps` (`get_action_values`)
    - `_motion_lib.load_motions`
    - `agent.experience_buffer` after `play_steps`
    - `batch_dict` after `play_steps`

- where is data stored?
    - 


- todo: physics engine stuff, where are things defined?
- todo: value

`batch_size = horizon_length * num_actors * num_agents`
batch_size must be multiple of minibatch_size, and minibatch_size should be a power of 2
num_agents is 1
`num_envs = num_actors`


- how many instances/handles to isaac gym binary exist?
    - should be one, which is a mutex set in `BaseTask.__init__`, `self.gym = gymapi.acquire_gym()`
    - 
- 


# soccer dataset:

pose:
global_orient = (22, 1032, 3)
body_pose = (22, 1032, 69)
transl = (22, 1032, 3)
betas = (22, 10)

cameras:
k = (1032, 5)
K = (1032, 3, 3)
R = (1032, 3, 3)
t = (1032, 3)
Rt = (1032, 3, 4)

joe data ocr
skating model