// Generated by gencpp from file a_b_action_server/a_bGoal.msg
// DO NOT EDIT!


#ifndef A_B_ACTION_SERVER_MESSAGE_A_BGOAL_H
#define A_B_ACTION_SERVER_MESSAGE_A_BGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace a_b_action_server
{
template <class ContainerAllocator>
struct a_bGoal_
{
  typedef a_bGoal_<ContainerAllocator> Type;

  a_bGoal_()
    : force(0.0)
    , goal_distance(0.0)  {
    }
  a_bGoal_(const ContainerAllocator& _alloc)
    : force(0.0)
    , goal_distance(0.0)  {
  (void)_alloc;
    }



   typedef float _force_type;
  _force_type force;

   typedef float _goal_distance_type;
  _goal_distance_type goal_distance;




  typedef boost::shared_ptr< ::a_b_action_server::a_bGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::a_b_action_server::a_bGoal_<ContainerAllocator> const> ConstPtr;

}; // struct a_bGoal_

typedef ::a_b_action_server::a_bGoal_<std::allocator<void> > a_bGoal;

typedef boost::shared_ptr< ::a_b_action_server::a_bGoal > a_bGoalPtr;
typedef boost::shared_ptr< ::a_b_action_server::a_bGoal const> a_bGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::a_b_action_server::a_bGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::a_b_action_server::a_bGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace a_b_action_server

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'a_b_action_server': ['/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_b_action_server/msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::a_b_action_server::a_bGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::a_b_action_server::a_bGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::a_b_action_server::a_bGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::a_b_action_server::a_bGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::a_b_action_server::a_bGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::a_b_action_server::a_bGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::a_b_action_server::a_bGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "051f5410092db6d015c1933bfc45c200";
  }

  static const char* value(const ::a_b_action_server::a_bGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x051f5410092db6d0ULL;
  static const uint64_t static_value2 = 0x15c1933bfc45c200ULL;
};

template<class ContainerAllocator>
struct DataType< ::a_b_action_server::a_bGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a_b_action_server/a_bGoal";
  }

  static const char* value(const ::a_b_action_server::a_bGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::a_b_action_server::a_bGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
float32 force\n\
float32 goal_distance\n\
";
  }

  static const char* value(const ::a_b_action_server::a_bGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::a_b_action_server::a_bGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.force);
      stream.next(m.goal_distance);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct a_bGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::a_b_action_server::a_bGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::a_b_action_server::a_bGoal_<ContainerAllocator>& v)
  {
    s << indent << "force: ";
    Printer<float>::stream(s, indent + "  ", v.force);
    s << indent << "goal_distance: ";
    Printer<float>::stream(s, indent + "  ", v.goal_distance);
  }
};

} // namespace message_operations
} // namespace ros

#endif // A_B_ACTION_SERVER_MESSAGE_A_BGOAL_H
