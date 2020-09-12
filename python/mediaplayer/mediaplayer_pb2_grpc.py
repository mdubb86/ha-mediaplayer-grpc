# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import mediaplayer_pb2 as mediaplayer__pb2


class MediaPlayerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetVolume = channel.unary_unary(
                '/mediaplayer.MediaPlayer/SetVolume',
                request_serializer=mediaplayer__pb2.SetVolumeReq.SerializeToString,
                response_deserializer=mediaplayer__pb2.SetVolumeRes.FromString,
                )
        self.StreamUpdates = channel.unary_stream(
                '/mediaplayer.MediaPlayer/StreamUpdates',
                request_serializer=mediaplayer__pb2.StreamUpdatesReq.SerializeToString,
                response_deserializer=mediaplayer__pb2.Update.FromString,
                )


class MediaPlayerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SetVolume(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamUpdates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MediaPlayerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetVolume': grpc.unary_unary_rpc_method_handler(
                    servicer.SetVolume,
                    request_deserializer=mediaplayer__pb2.SetVolumeReq.FromString,
                    response_serializer=mediaplayer__pb2.SetVolumeRes.SerializeToString,
            ),
            'StreamUpdates': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamUpdates,
                    request_deserializer=mediaplayer__pb2.StreamUpdatesReq.FromString,
                    response_serializer=mediaplayer__pb2.Update.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mediaplayer.MediaPlayer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MediaPlayer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SetVolume(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mediaplayer.MediaPlayer/SetVolume',
            mediaplayer__pb2.SetVolumeReq.SerializeToString,
            mediaplayer__pb2.SetVolumeRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamUpdates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/mediaplayer.MediaPlayer/StreamUpdates',
            mediaplayer__pb2.StreamUpdatesReq.SerializeToString,
            mediaplayer__pb2.Update.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
