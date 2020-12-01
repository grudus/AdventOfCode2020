package com.grudus.adventofcode;

import lombok.SneakyThrows;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Utils {

    @SneakyThrows
    public static List<String> readFileInput(String day) {
        return Files.readAllLines(Path.of(String.format("src/main/java/com/grudus/adventofcode/day%s/input.txt", day)));
    }

    public static List<String> readFileInput(Class<?> classDay) {
        var day = classDay.getSimpleName().substring(3);
        return readFileInput(day);
    }
}
