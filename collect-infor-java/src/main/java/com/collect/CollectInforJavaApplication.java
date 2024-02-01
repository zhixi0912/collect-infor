package com.collect;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@SpringBootApplication
public class CollectInforJavaApplication {

    public static void main(String[] args) {
        SpringApplication.run(CollectInforJavaApplication.class, args);
    }
    @GetMapping("/")
    public String index() {
        return "hello world!";
    }
}
