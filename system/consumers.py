
from demo.models import Drone, DroneTest
from demo.serializers import DroneTestSerializer
from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.mixins import ListModelMixin


class SystemTestConsumer(ListModelMixin, GenericAsyncAPIConsumer):

    queryset = DroneTest.objects.all()
    serializer_class = DroneTestSerializer
    permissions = (permissions.AllowAny,)

    async def connect(self, **kwargs):
        await self.model_change.subscribe()
        await super().connect()

    @model_observer(DroneTest)
    async def model_change(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @model_change.serializer
    def model_serialize(self, instance, action, **kwargs):
        return dict(data=DroneSerializer(instance=instance).data, action=action.value)
