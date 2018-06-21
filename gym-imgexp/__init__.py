from gym.envs.registration import register

register(
    id='imgexp-v0',
    entry_point='gym_imgexp.envs:ImgexpEnv',
)
register(
    id='imgexp-extrahard-v0',
    entry_point='gym_imgexp.envs:ImgexpExtraHardEnv',
)