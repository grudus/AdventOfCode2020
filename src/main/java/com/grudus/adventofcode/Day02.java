package com.grudus.adventofcode;

import io.vavr.collection.List;

import java.util.regex.Pattern;

import static java.lang.Integer.parseInt;

// --- Day 2: Password Philosophy ---
public class Day02 extends Day<Integer> {
    private final static Pattern PASSWORD_POLICY_PATTERN = Pattern.compile("(\\d+)-(\\d+) (\\w): (\\w+)");

    @Override
    public Integer firstStar(List<String> input) {
        return input
                .map(line -> Utils.findRegexGroups(PASSWORD_POLICY_PATTERN, line))
                .map(groups -> PolicyAndPassword.fromGroups(groups.toArray(String[]::new)))
                .count(PolicyAndPassword::isFirstJobValid);
    }

    @Override
    public Integer secondStar(List<String> input) {
        return input
                .map(line -> Utils.findRegexGroups(PASSWORD_POLICY_PATTERN, line))
                .map(groups -> PolicyAndPassword.fromGroups(groups.toArray(String[]::new)))
                .count(PolicyAndPassword::isOfficialTobogganCorporateAuthenticationSystemValid);
    }


    record PolicyAndPassword(int rangeStart, int rangeEnd, char letter, String password) {
        static PolicyAndPassword fromGroups(String[] groups) {
            return new PolicyAndPassword(parseInt(groups[0]), parseInt(groups[1]), groups[2].charAt(0), groups[3]);
        }

        boolean isFirstJobValid() {
            long count = password.chars()
                    .filter(character -> character == letter)
                    .count();
            return count >= rangeStart && count <= rangeEnd;
        }

        boolean isOfficialTobogganCorporateAuthenticationSystemValid() {
            return ((password.charAt(rangeStart - 1) == letter ? 1 : 0)
                    + (password.charAt(rangeEnd - 1) == letter ? 1 : 0)) == 1;
        }
    }
}
