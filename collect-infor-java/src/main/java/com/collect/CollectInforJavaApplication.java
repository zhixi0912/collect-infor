package com.collect;

import com.collect.entity.User;
import com.collect.mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@SpringBootApplication
public class CollectInforJavaApplication {

    @Autowired
    public UserMapper userMapper;
    public static void main(String[] args) {
        SpringApplication.run(CollectInforJavaApplication.class, args);
    }
    @GetMapping("/user/list")
    public List<User> index() {
        return userMapper.findAll();
    }

    @PostMapping('/user/add')
    public index() {
        return "OK";
    }
}
