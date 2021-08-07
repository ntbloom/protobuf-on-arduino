/* Automatically generated nanopb header */
/* Generated by nanopb-0.4.6-dev at Sat Aug  7 00:28:58 2021. */

#ifndef PB_RAINCOUNTER_PB_H_INCLUDED
#define PB_RAINCOUNTER_PB_H_INCLUDED
#include <pb.h>

#if PB_PROTO_HEADER_VERSION != 40
#error Regenerate this file with the current version of nanopb generator.
#endif

/* Enum definitions */
typedef enum _DataPacket_PacketType { 
    DataPacket_PacketType_TEMPERATURE = 0 
} DataPacket_PacketType;

typedef enum _EventPacket_PacketType { 
    EventPacket_PacketType_TIPPER_CLICK = 0, 
    EventPacket_PacketType_SOFT_RESET = 1, 
    EventPacket_PacketType_HARD_RESET = 2, 
    EventPacket_PacketType_START_PAUSE = 3, 
    EventPacket_PacketType_STOP_PAUSE = 4 
} EventPacket_PacketType;

/* Struct definitions */
typedef struct _DataPacket { 
    DataPacket_PacketType packetType; 
    int32_t value; 
} DataPacket;

typedef struct _EventPacket { 
    EventPacket_PacketType packetType; 
} EventPacket;


/* Helper constants for enums */
#define _DataPacket_PacketType_MIN DataPacket_PacketType_TEMPERATURE
#define _DataPacket_PacketType_MAX DataPacket_PacketType_TEMPERATURE
#define _DataPacket_PacketType_ARRAYSIZE ((DataPacket_PacketType)(DataPacket_PacketType_TEMPERATURE+1))

#define _EventPacket_PacketType_MIN EventPacket_PacketType_TIPPER_CLICK
#define _EventPacket_PacketType_MAX EventPacket_PacketType_STOP_PAUSE
#define _EventPacket_PacketType_ARRAYSIZE ((EventPacket_PacketType)(EventPacket_PacketType_STOP_PAUSE+1))


#ifdef __cplusplus
extern "C" {
#endif

/* Initializer values for message structs */
#define DataPacket_init_default                  {_DataPacket_PacketType_MIN, 0}
#define EventPacket_init_default                 {_EventPacket_PacketType_MIN}
#define DataPacket_init_zero                     {_DataPacket_PacketType_MIN, 0}
#define EventPacket_init_zero                    {_EventPacket_PacketType_MIN}

/* Field tags (for use in manual encoding/decoding) */
#define DataPacket_packetType_tag                1
#define DataPacket_value_tag                     2
#define EventPacket_packetType_tag               1

/* Struct field encoding specification for nanopb */
#define DataPacket_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UENUM,    packetType,        1) \
X(a, STATIC,   SINGULAR, INT32,    value,             2)
#define DataPacket_CALLBACK NULL
#define DataPacket_DEFAULT NULL

#define EventPacket_FIELDLIST(X, a) \
X(a, STATIC,   SINGULAR, UENUM,    packetType,        1)
#define EventPacket_CALLBACK NULL
#define EventPacket_DEFAULT NULL

extern const pb_msgdesc_t DataPacket_msg;
extern const pb_msgdesc_t EventPacket_msg;

/* Defines for backwards compatibility with code written before nanopb-0.4.0 */
#define DataPacket_fields &DataPacket_msg
#define EventPacket_fields &EventPacket_msg

/* Maximum encoded size of messages (where known) */
#define DataPacket_size                          13
#define EventPacket_size                         2

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif