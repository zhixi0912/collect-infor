package com.collect.entity;

import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.web.bind.annotation.RestController;

import java.security.Timestamp;
import java.util.Date;

@Data
//@NoArgsConstructor
//@AllArgsConstructor
public class User {
    private Integer id;
    private String username;
    private String password;
    private String nickname;
    private String email;
    private String phone;
    private String gender;
    private Integer bank_id;
    private Integer card_id;
    private String address;
    private String wx_id;
    private String avatar;
    @JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss", timezone = "GMT+8")
    private Date create_time;
}
