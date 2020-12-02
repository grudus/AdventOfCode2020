package com.grudus.adventofcode;

import lombok.SneakyThrows;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Utils {

    @SneakyThrows
    public static List<String> readFileInput(String day) {
        return Files.readAllLines(Path.of(String.format("src/main/java/com/grudus/adventofcode/day%s/input.txt", day)));
    }

    public static List<String> readFileInput(Class<?> classDay) {
        var day = classDay.getSimpleName().substring(3);
        return readFileInput(day);
    }

    public static List<String> findRegexGroups(Pattern pattern, String text) {
        Matcher matcher = pattern.matcher(text);
        List<String> groups = new ArrayList<>();

        while (matcher.find()) {
            for (int i = 1; i <= matcher.groupCount(); i++) {
                groups.add(matcher.group(i));
            }
        }
        return groups;
    }

}
