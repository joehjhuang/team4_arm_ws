// Generated by gencpp from file a_a_action_server/a_aFeedback.msg
// DO NOT EDIT!


#ifndef A_A_ACTION_SERVER_MESSAGE_A_AFEEDBACK_H
#define A_A_ACTION_SERVER_MESSAGE_A_AFEEDBACK_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace a_a_action_server
{
template <class ContainerAllocator>
struct a_aFeedback_
{
  typedef a_aFeedback_<ContainerAllocator> Type;

  a_aFeedback_()
    {
    }
  a_aFeedback_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }






  typedef boost::shared_ptr< ::a_a_action_server::a_aFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::a_a_action_server::a_aFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct a_aFeedback_

typedef ::a_a_action_server::a_aFeedback_<std::allocator<void> > a_aFeedback;

typedef boost::shared_ptr< ::a_a_action_server::a_aFeedback > a_aFeedbackPtr;
typedef boost::shared_ptr< ::a_a_action_server::a_aFeedback const> a_aFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::a_a_action_server::a_aFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::a_a_action_server::a_aFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace a_a_action_server

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'a_a_action_server': ['/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_a_action_server/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::a_a_action_server::a_aFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::a_a_action_server::a_aFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::a_a_action_server::a_aFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::a_a_action_server::a_aFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::a_a_action_server::a_aFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::a_a_action_server::a_aFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::a_a_action_server::a_aFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::a_a_action_server::a_aFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::a_a_action_server::a_aFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a_a_action_server/a_aFeedback";
  }

  static const char* value(const ::a_a_action_server::a_aFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::a_a_action_server::a_aFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#feedback\n\
\n\
";
  }

  static const char* value(const ::a_a_action_server::a_aFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::a_a_action_server::a_aFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct a_aFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::a_a_action_server::a_aFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::a_a_action_server::a_aFeedback_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // A_A_ACTION_SERVER_MESSAGE_A_AFEEDBACK_H
