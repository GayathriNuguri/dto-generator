package com.sample.dtoConverter.controller;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.sample.dtoConverter.service.DtoService;

@RestController
public class DtoController {

	@Autowired
	private DtoService dtoService;

	@PostMapping("/generate-dto")
	public ResponseEntity<String> generateDto(@RequestBody Map<String, String> request) {
		String className = request.getOrDefault("className", "MyDTO");
		String requirement = request.getOrDefault("requirement", "");
		String resp = dtoService.generateDto(className, requirement);
		return ResponseEntity.status(HttpStatus.OK).header("Content-Type", "text/plain; charset=UTF-8").body(resp);
	}

}
