// Generated by gencpp from file interbotix_xs_msgs/RobotInfoResponse.msg
// DO NOT EDIT!


#ifndef INTERBOTIX_XS_MSGS_MESSAGE_ROBOTINFORESPONSE_H
#define INTERBOTIX_XS_MSGS_MESSAGE_ROBOTINFORESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace interbotix_xs_msgs
{
template <class ContainerAllocator>
struct RobotInfoResponse_
{
  typedef RobotInfoResponse_<ContainerAllocator> Type;

  RobotInfoResponse_()
    : mode()
    , profile_type()
    , joint_names()
    , joint_ids()
    , joint_lower_limits()
    , joint_upper_limits()
    , joint_velocity_limits()
    , joint_sleep_positions()
    , joint_state_indices()
    , num_joints(0)
    , name()  {
    }
  RobotInfoResponse_(const ContainerAllocator& _alloc)
    : mode(_alloc)
    , profile_type(_alloc)
    , joint_names(_alloc)
    , joint_ids(_alloc)
    , joint_lower_limits(_alloc)
    , joint_upper_limits(_alloc)
    , joint_velocity_limits(_alloc)
    , joint_sleep_positions(_alloc)
    , joint_state_indices(_alloc)
    , num_joints(0)
    , name(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _mode_type;
  _mode_type mode;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _profile_type_type;
  _profile_type_type profile_type;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _joint_names_type;
  _joint_names_type joint_names;

   typedef std::vector<int16_t, typename ContainerAllocator::template rebind<int16_t>::other >  _joint_ids_type;
  _joint_ids_type joint_ids;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _joint_lower_limits_type;
  _joint_lower_limits_type joint_lower_limits;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _joint_upper_limits_type;
  _joint_upper_limits_type joint_upper_limits;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _joint_velocity_limits_type;
  _joint_velocity_limits_type joint_velocity_limits;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _joint_sleep_positions_type;
  _joint_sleep_positions_type joint_sleep_positions;

   typedef std::vector<int16_t, typename ContainerAllocator::template rebind<int16_t>::other >  _joint_state_indices_type;
  _joint_state_indices_type joint_state_indices;

   typedef int16_t _num_joints_type;
  _num_joints_type num_joints;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _name_type;
  _name_type name;





  typedef boost::shared_ptr< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> const> ConstPtr;

}; // struct RobotInfoResponse_

typedef ::interbotix_xs_msgs::RobotInfoResponse_<std::allocator<void> > RobotInfoResponse;

typedef boost::shared_ptr< ::interbotix_xs_msgs::RobotInfoResponse > RobotInfoResponsePtr;
typedef boost::shared_ptr< ::interbotix_xs_msgs::RobotInfoResponse const> RobotInfoResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator1> & lhs, const ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator2> & rhs)
{
  return lhs.mode == rhs.mode &&
    lhs.profile_type == rhs.profile_type &&
    lhs.joint_names == rhs.joint_names &&
    lhs.joint_ids == rhs.joint_ids &&
    lhs.joint_lower_limits == rhs.joint_lower_limits &&
    lhs.joint_upper_limits == rhs.joint_upper_limits &&
    lhs.joint_velocity_limits == rhs.joint_velocity_limits &&
    lhs.joint_sleep_positions == rhs.joint_sleep_positions &&
    lhs.joint_state_indices == rhs.joint_state_indices &&
    lhs.num_joints == rhs.num_joints &&
    lhs.name == rhs.name;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator1> & lhs, const ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace interbotix_xs_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "23accaf5885f241d75742c1e9c1c0448";
  }

  static const char* value(const ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x23accaf5885f241dULL;
  static const uint64_t static_value2 = 0x75742c1e9c1c0448ULL;
};

template<class ContainerAllocator>
struct DataType< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "interbotix_xs_msgs/RobotInfoResponse";
  }

  static const char* value(const ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string mode                              # the operating mode for the specified joint group or joint\n"
"string profile_type                      # the profile type for the specified joint group or joint\n"
"string[] joint_names                     # the name of each joint in a group or just the specified joint\n"
"int16[] joint_ids                        # the Dynamixel ID for each joint in a group or for the specified joint\n"
"float32[] joint_lower_limits             # the lower limit [radians] for each joint in a group or for the specified joint (taken from URDF)\n"
"float32[] joint_upper_limits             # the upper limit [radians] for each joint in a group or for the specified joint (taken from URDF)\n"
"float32[] joint_velocity_limits          # the velocity limit [rad/s] for each joint in a group or for the specified joint (taken from URDF)\n"
"float32[] joint_sleep_positions          # the sleep position [rad] for each joint in a group or for the specified joint\n"
"int16[] joint_state_indices              # index for each joint in a group or for the specified joint in the published JointState message\n"
"int16 num_joints                         # the number of joints in a group or 1\n"
"string[] name                            # the name of the group or joint requested; if group was 'all', returns the names of all groups\n"
"\n"
;
  }

  static const char* value(const ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.mode);
      stream.next(m.profile_type);
      stream.next(m.joint_names);
      stream.next(m.joint_ids);
      stream.next(m.joint_lower_limits);
      stream.next(m.joint_upper_limits);
      stream.next(m.joint_velocity_limits);
      stream.next(m.joint_sleep_positions);
      stream.next(m.joint_state_indices);
      stream.next(m.num_joints);
      stream.next(m.name);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RobotInfoResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::interbotix_xs_msgs::RobotInfoResponse_<ContainerAllocator>& v)
  {
    s << indent << "mode: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.mode);
    s << indent << "profile_type: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.profile_type);
    s << indent << "joint_names[]" << std::endl;
    for (size_t i = 0; i < v.joint_names.size(); ++i)
    {
      s << indent << "  joint_names[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.joint_names[i]);
    }
    s << indent << "joint_ids[]" << std::endl;
    for (size_t i = 0; i < v.joint_ids.size(); ++i)
    {
      s << indent << "  joint_ids[" << i << "]: ";
      Printer<int16_t>::stream(s, indent + "  ", v.joint_ids[i]);
    }
    s << indent << "joint_lower_limits[]" << std::endl;
    for (size_t i = 0; i < v.joint_lower_limits.size(); ++i)
    {
      s << indent << "  joint_lower_limits[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.joint_lower_limits[i]);
    }
    s << indent << "joint_upper_limits[]" << std::endl;
    for (size_t i = 0; i < v.joint_upper_limits.size(); ++i)
    {
      s << indent << "  joint_upper_limits[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.joint_upper_limits[i]);
    }
    s << indent << "joint_velocity_limits[]" << std::endl;
    for (size_t i = 0; i < v.joint_velocity_limits.size(); ++i)
    {
      s << indent << "  joint_velocity_limits[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.joint_velocity_limits[i]);
    }
    s << indent << "joint_sleep_positions[]" << std::endl;
    for (size_t i = 0; i < v.joint_sleep_positions.size(); ++i)
    {
      s << indent << "  joint_sleep_positions[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.joint_sleep_positions[i]);
    }
    s << indent << "joint_state_indices[]" << std::endl;
    for (size_t i = 0; i < v.joint_state_indices.size(); ++i)
    {
      s << indent << "  joint_state_indices[" << i << "]: ";
      Printer<int16_t>::stream(s, indent + "  ", v.joint_state_indices[i]);
    }
    s << indent << "num_joints: ";
    Printer<int16_t>::stream(s, indent + "  ", v.num_joints);
    s << indent << "name[]" << std::endl;
    for (size_t i = 0; i < v.name.size(); ++i)
    {
      s << indent << "  name[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // INTERBOTIX_XS_MSGS_MESSAGE_ROBOTINFORESPONSE_H
