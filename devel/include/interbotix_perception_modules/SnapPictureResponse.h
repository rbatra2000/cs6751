// Generated by gencpp from file interbotix_perception_modules/SnapPictureResponse.msg
// DO NOT EDIT!


#ifndef INTERBOTIX_PERCEPTION_MODULES_MESSAGE_SNAPPICTURERESPONSE_H
#define INTERBOTIX_PERCEPTION_MODULES_MESSAGE_SNAPPICTURERESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace interbotix_perception_modules
{
template <class ContainerAllocator>
struct SnapPictureResponse_
{
  typedef SnapPictureResponse_<ContainerAllocator> Type;

  SnapPictureResponse_()
    : success(false)
    , filepath()  {
    }
  SnapPictureResponse_(const ContainerAllocator& _alloc)
    : success(false)
    , filepath(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _filepath_type;
  _filepath_type filepath;





  typedef boost::shared_ptr< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> const> ConstPtr;

}; // struct SnapPictureResponse_

typedef ::interbotix_perception_modules::SnapPictureResponse_<std::allocator<void> > SnapPictureResponse;

typedef boost::shared_ptr< ::interbotix_perception_modules::SnapPictureResponse > SnapPictureResponsePtr;
typedef boost::shared_ptr< ::interbotix_perception_modules::SnapPictureResponse const> SnapPictureResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator1> & lhs, const ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator2> & rhs)
{
  return lhs.success == rhs.success &&
    lhs.filepath == rhs.filepath;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator1> & lhs, const ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace interbotix_perception_modules

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1af3a23d59f26a54fd4c297f9a0f8ee4";
  }

  static const char* value(const ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1af3a23d59f26a54ULL;
  static const uint64_t static_value2 = 0xfd4c297f9a0f8ee4ULL;
};

template<class ContainerAllocator>
struct DataType< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "interbotix_perception_modules/SnapPictureResponse";
  }

  static const char* value(const ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n"
"string filepath\n"
;
  }

  static const char* value(const ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
      stream.next(m.filepath);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SnapPictureResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::interbotix_perception_modules::SnapPictureResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
    s << indent << "filepath: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.filepath);
  }
};

} // namespace message_operations
} // namespace ros

#endif // INTERBOTIX_PERCEPTION_MODULES_MESSAGE_SNAPPICTURERESPONSE_H
