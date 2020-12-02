package com.grudus.adventofcode;

import io.vavr.collection.List;

import java.util.regex.Pattern;

import static io.vavr.collection.List.ofAll;
import static java.lang.Integer.parseInt;

// --- Day 2: Password Philosophy ---
public class Day02 {
    private final static Pattern PASSWORD_POLICY_PATTERN = Pattern.compile("(\\d+)-(\\d+) (\\w): (\\w+)");

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


    public static int firstStar(List<String> input) {
        return input
                .map(line -> Utils.findRegexGroups(PASSWORD_POLICY_PATTERN, line))
                .map(groups -> PolicyAndPassword.fromGroups(groups.toArray(String[]::new)))
                .count(PolicyAndPassword::isFirstJobValid);
    }

    public static int secondStar(List<String> input) {
        return input
                .map(line -> Utils.findRegexGroups(PASSWORD_POLICY_PATTERN, line))
                .map(groups -> PolicyAndPassword.fromGroups(groups.toArray(String[]::new)))
                .count(PolicyAndPassword::isOfficialTobogganCorporateAuthenticationSystemValid);
    }


    public static void main(String[] args) {
        var input = Utils.readFileInput(Day02.class);

        System.out.println(firstStar(ofAll(input)));
        System.out.println(secondStar(ofAll(input)));
    }
}
