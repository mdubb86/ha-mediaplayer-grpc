// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package mediaplayer

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion7

// MediaPlayerClient is the client API for MediaPlayer service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type MediaPlayerClient interface {
	Communicate(ctx context.Context, opts ...grpc.CallOption) (MediaPlayer_CommunicateClient, error)
}

type mediaPlayerClient struct {
	cc grpc.ClientConnInterface
}

func NewMediaPlayerClient(cc grpc.ClientConnInterface) MediaPlayerClient {
	return &mediaPlayerClient{cc}
}

var mediaPlayerCommunicateStreamDesc = &grpc.StreamDesc{
	StreamName:    "Communicate",
	ServerStreams: true,
	ClientStreams: true,
}

func (c *mediaPlayerClient) Communicate(ctx context.Context, opts ...grpc.CallOption) (MediaPlayer_CommunicateClient, error) {
	stream, err := c.cc.NewStream(ctx, mediaPlayerCommunicateStreamDesc, "/mediaplayer.MediaPlayer/Communicate", opts...)
	if err != nil {
		return nil, err
	}
	x := &mediaPlayerCommunicateClient{stream}
	return x, nil
}

type MediaPlayer_CommunicateClient interface {
	Send(*Request) error
	Recv() (*Response, error)
	grpc.ClientStream
}

type mediaPlayerCommunicateClient struct {
	grpc.ClientStream
}

func (x *mediaPlayerCommunicateClient) Send(m *Request) error {
	return x.ClientStream.SendMsg(m)
}

func (x *mediaPlayerCommunicateClient) Recv() (*Response, error) {
	m := new(Response)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

// MediaPlayerService is the service API for MediaPlayer service.
// Fields should be assigned to their respective handler implementations only before
// RegisterMediaPlayerService is called.  Any unassigned fields will result in the
// handler for that method returning an Unimplemented error.
type MediaPlayerService struct {
	Communicate func(MediaPlayer_CommunicateServer) error
}

func (s *MediaPlayerService) communicate(_ interface{}, stream grpc.ServerStream) error {
	return s.Communicate(&mediaPlayerCommunicateServer{stream})
}

type MediaPlayer_CommunicateServer interface {
	Send(*Response) error
	Recv() (*Request, error)
	grpc.ServerStream
}

type mediaPlayerCommunicateServer struct {
	grpc.ServerStream
}

func (x *mediaPlayerCommunicateServer) Send(m *Response) error {
	return x.ServerStream.SendMsg(m)
}

func (x *mediaPlayerCommunicateServer) Recv() (*Request, error) {
	m := new(Request)
	if err := x.ServerStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

// RegisterMediaPlayerService registers a service implementation with a gRPC server.
func RegisterMediaPlayerService(s grpc.ServiceRegistrar, srv *MediaPlayerService) {
	srvCopy := *srv
	if srvCopy.Communicate == nil {
		srvCopy.Communicate = func(MediaPlayer_CommunicateServer) error {
			return status.Errorf(codes.Unimplemented, "method Communicate not implemented")
		}
	}
	sd := grpc.ServiceDesc{
		ServiceName: "mediaplayer.MediaPlayer",
		Methods:     []grpc.MethodDesc{},
		Streams: []grpc.StreamDesc{
			{
				StreamName:    "Communicate",
				Handler:       srvCopy.communicate,
				ServerStreams: true,
				ClientStreams: true,
			},
		},
		Metadata: "mediaplayer.proto",
	}

	s.RegisterService(&sd, nil)
}
