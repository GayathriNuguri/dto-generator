package com.sample.dtoConverter.service;

import java.util.HashMap;
import java.util.Map;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class DtoService {

	private final RestTemplate restTemplate = new RestTemplate();

	public String generateDto(String className, String requirement) {
		String flaskUrl = "http://localhost:5000/generate-dto";

		Map<String, String> requestBody = new HashMap<>();
		requestBody.put("className", className);
		requestBody.put("requirement", requirement);

		ResponseEntity<Map> response = restTemplate.postForEntity(flaskUrl, requestBody, Map.class);

		return (String) response.getBody().get("dto");
	}
}
