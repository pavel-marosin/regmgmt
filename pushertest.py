import pusher

pusher_client = pusher.Pusher(
  app_id='366194',
  key='0fbca878a6fe2601bbb2',
  secret='1dffbd2510f9cac8d966',
  cluster='us2',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})