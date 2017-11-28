# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "a_halt_action_server: 7 messages, 0 services")

set(MSG_I_FLAGS "-Ia_halt_action_server:/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg;-Iactionlib_msgs:/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(a_halt_action_server_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg" NAME_WE)
add_custom_target(_a_halt_action_server_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "a_halt_action_server" "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg" ""
)

get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg" NAME_WE)
add_custom_target(_a_halt_action_server_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "a_halt_action_server" "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg" "a_halt_action_server/a_haltGoal:actionlib_msgs/GoalID:std_msgs/Header"
)

get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg" NAME_WE)
add_custom_target(_a_halt_action_server_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "a_halt_action_server" "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg" ""
)

get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg" NAME_WE)
add_custom_target(_a_halt_action_server_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "a_halt_action_server" "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg" "a_halt_action_server/a_haltResult:actionlib_msgs/GoalID:std_msgs/Header:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltAction.msg" NAME_WE)
add_custom_target(_a_halt_action_server_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "a_halt_action_server" "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltAction.msg" "a_halt_action_server/a_haltResult:actionlib_msgs/GoalStatus:a_halt_action_server/a_haltGoal:a_halt_action_server/a_haltActionFeedback:std_msgs/Header:a_halt_action_server/a_haltFeedback:actionlib_msgs/GoalID:a_halt_action_server/a_haltActionGoal:a_halt_action_server/a_haltActionResult"
)

get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg" NAME_WE)
add_custom_target(_a_halt_action_server_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "a_halt_action_server" "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg" ""
)

get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg" NAME_WE)
add_custom_target(_a_halt_action_server_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "a_halt_action_server" "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg" "a_halt_action_server/a_haltFeedback:actionlib_msgs/GoalID:std_msgs/Header:actionlib_msgs/GoalStatus"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_cpp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_cpp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_cpp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltAction.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_cpp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_cpp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_cpp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/a_halt_action_server
)

### Generating Services

### Generating Module File
_generate_module_cpp(a_halt_action_server
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/a_halt_action_server
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(a_halt_action_server_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(a_halt_action_server_generate_messages a_halt_action_server_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_cpp _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_cpp _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_cpp _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_cpp _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltAction.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_cpp _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_cpp _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_cpp _a_halt_action_server_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(a_halt_action_server_gencpp)
add_dependencies(a_halt_action_server_gencpp a_halt_action_server_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS a_halt_action_server_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_eus(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_eus(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_eus(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltAction.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_eus(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_eus(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_eus(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/a_halt_action_server
)

### Generating Services

### Generating Module File
_generate_module_eus(a_halt_action_server
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/a_halt_action_server
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(a_halt_action_server_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(a_halt_action_server_generate_messages a_halt_action_server_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_eus _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_eus _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_eus _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_eus _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltAction.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_eus _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_eus _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_eus _a_halt_action_server_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(a_halt_action_server_geneus)
add_dependencies(a_halt_action_server_geneus a_halt_action_server_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS a_halt_action_server_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_lisp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_lisp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_lisp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltAction.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_lisp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_lisp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_lisp(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/a_halt_action_server
)

### Generating Services

### Generating Module File
_generate_module_lisp(a_halt_action_server
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/a_halt_action_server
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(a_halt_action_server_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(a_halt_action_server_generate_messages a_halt_action_server_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_lisp _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_lisp _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_lisp _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_lisp _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltAction.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_lisp _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_lisp _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_lisp _a_halt_action_server_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(a_halt_action_server_genlisp)
add_dependencies(a_halt_action_server_genlisp a_halt_action_server_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS a_halt_action_server_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_nodejs(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_nodejs(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_nodejs(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltAction.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_nodejs(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_nodejs(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_nodejs(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/a_halt_action_server
)

### Generating Services

### Generating Module File
_generate_module_nodejs(a_halt_action_server
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/a_halt_action_server
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(a_halt_action_server_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(a_halt_action_server_generate_messages a_halt_action_server_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_nodejs _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_nodejs _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_nodejs _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_nodejs _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltAction.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_nodejs _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_nodejs _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_nodejs _a_halt_action_server_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(a_halt_action_server_gennodejs)
add_dependencies(a_halt_action_server_gennodejs a_halt_action_server_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS a_halt_action_server_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_py(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_py(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_py(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltAction.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg;/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_py(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_py(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/a_halt_action_server
)
_generate_msg_py(a_halt_action_server
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/a_halt_action_server
)

### Generating Services

### Generating Module File
_generate_module_py(a_halt_action_server
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/a_halt_action_server
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(a_halt_action_server_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(a_halt_action_server_generate_messages a_halt_action_server_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltGoal.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_py _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionGoal.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_py _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltResult.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_py _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionResult.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_py _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltAction.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_py _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltFeedback.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_py _a_halt_action_server_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/joehuang/Documents/MIT/2.12/team4_arm_ws/devel/share/a_halt_action_server/msg/a_haltActionFeedback.msg" NAME_WE)
add_dependencies(a_halt_action_server_generate_messages_py _a_halt_action_server_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(a_halt_action_server_genpy)
add_dependencies(a_halt_action_server_genpy a_halt_action_server_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS a_halt_action_server_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/a_halt_action_server)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/a_halt_action_server
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(a_halt_action_server_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(a_halt_action_server_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(a_halt_action_server_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/a_halt_action_server)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/a_halt_action_server
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(a_halt_action_server_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(a_halt_action_server_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(a_halt_action_server_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/a_halt_action_server)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/a_halt_action_server
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(a_halt_action_server_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(a_halt_action_server_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(a_halt_action_server_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/a_halt_action_server)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/a_halt_action_server
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(a_halt_action_server_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(a_halt_action_server_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(a_halt_action_server_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/a_halt_action_server)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/a_halt_action_server\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/a_halt_action_server
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(a_halt_action_server_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(a_halt_action_server_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(a_halt_action_server_generate_messages_py std_msgs_generate_messages_py)
endif()
