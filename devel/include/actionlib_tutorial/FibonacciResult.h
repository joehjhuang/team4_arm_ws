// Generated by gencpp from file actionlib_tutorial/FibonacciResult.msg
// DO NOT EDIT!


#ifndef ACTIONLIB_TUTORIAL_MESSAGE_FIBONACCIRESULT_H
#define ACTIONLIB_TUTORIAL_MESSAGE_FIBONACCIRESULT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace actionlib_tutorial
{
template <class ContainerAllocator>
struct FibonacciResult_
{
  typedef FibonacciResult_<ContainerAllocator> Type;

  FibonacciResult_()
    : sequence()  {
    }
  FibonacciResult_(const ContainerAllocator& _alloc)
    : sequence(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _sequence_type;
  _sequence_type sequence;




  typedef boost::shared_ptr< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> const> ConstPtr;

}; // struct FibonacciResult_

typedef ::actionlib_tutorial::FibonacciResult_<std::allocator<void> > FibonacciResult;

typedef boost::shared_ptr< ::actionlib_tutorial::FibonacciResult > FibonacciResultPtr;
typedef boost::shared_ptr< ::actionlib_tutorial::FibonacciResult const> FibonacciResultConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace actionlib_tutorial

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_tutorial': ['/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/actionlib_tutorial/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b81e37d2a31925a0e8ae261a8699cb79";
  }

  static const char* value(const ::actionlib_tutorial::FibonacciResult_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb81e37d2a31925a0ULL;
  static const uint64_t static_value2 = 0xe8ae261a8699cb79ULL;
};

template<class ContainerAllocator>
struct DataType< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "actionlib_tutorial/FibonacciResult";
  }

  static const char* value(const ::actionlib_tutorial::FibonacciResult_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
#result definition\n\
int32[] sequence\n\
";
  }

  static const char* value(const ::actionlib_tutorial::FibonacciResult_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.sequence);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct FibonacciResult_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::actionlib_tutorial::FibonacciResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::actionlib_tutorial::FibonacciResult_<ContainerAllocator>& v)
  {
    s << indent << "sequence[]" << std::endl;
    for (size_t i = 0; i < v.sequence.size(); ++i)
    {
      s << indent << "  sequence[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.sequence[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ACTIONLIB_TUTORIAL_MESSAGE_FIBONACCIRESULT_H
