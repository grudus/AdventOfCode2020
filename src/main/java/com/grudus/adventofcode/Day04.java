package com.grudus.adventofcode;

import io.vavr.collection.List;
import io.vavr.collection.Map;

import java.util.Objects;
import java.util.regex.Pattern;

import static java.lang.Integer.parseInt;

public class Day04 extends Day<Integer> {

    @Override
    public Integer firstStar(List<String> input) {
        return List.of(input.mkString("\n").split("\n\n"))
                .map(x -> x.split("\\s+"))
                .map(Passport::fromTokens)
                .filter(Objects::nonNull)
                .size();
    }

    @Override
    public Integer secondStar(List<String> input) {
        List<Passport> validPassports = List.of(input.mkString("\n").split("\n\n"))
                .map(x -> x.split("\\s+"))
                .map(Passport::fromTokens)
                .filter(Objects::nonNull);

        return validPassports.filter(Passport::hasValidValues).size();
    }


    record Passport(Integer byr, Integer iyr, Integer eyr, String hgt, String hcl, String ecl, String pid,
                    String cid) {
        public static Passport fromTokens(String[] tokens) {
            Map<String, String> values = List.of(tokens)
                    .map(token -> token.split(":"))
                    .toMap(token -> token[0], token -> token[1]);

            boolean isValid = List.of("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
                    .count(values::containsKey) == 7;

            if (!isValid) {
                return null;
            }

            return new Passport(
                    parseInt(values.getOrElse("byr", null)),
                    parseInt(values.getOrElse("iyr", null)),
                    parseInt(values.getOrElse("eyr", null)),
                    values.getOrElse("hgt", null),
                    values.getOrElse("hcl", null),
                    values.getOrElse("ecl", null),
                    values.getOrElse("pid", null),
                    values.getOrElse("cid", null)
            );
        }

        public boolean hasValidValues() {
            return
                    byr >= 1920 && byr <= 2002
                            && iyr >= 2010 && iyr <= 2020
                            && eyr >= 2020 && eyr <= 2030
                            && hasValidHeight()
                    && Pattern.compile("^#(?:[0-9a-f]{6})$").matcher(hcl).matches()
                    && Pattern.compile("amb|blu|brn|gry|grn|hzl|oth").matcher(ecl).matches()
                    && pid.length() == 9;
        }

        private boolean hasValidHeight() {
            final java.util.List<String> groups = Utils.findRegexGroups(Pattern.compile("(\\d+)(cm|in)"), hgt);
            if (groups.size() < 2)
                return false;
            int height = parseInt(groups.get(0));
            String unit = groups.get(1);

            return unit.equals("cm") ? (height >= 150 && height <= 193) : (height >= 59 && height <= 76);
        }
    }
}
