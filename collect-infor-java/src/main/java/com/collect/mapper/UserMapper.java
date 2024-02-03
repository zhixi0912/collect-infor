package com.collect.mapper;

import com.collect.entity.User;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface UserMapper {
//    SELECT * FROM sys_user
    @Select("SELECT * FROM sys_user")
    List<User> findAll();
}
