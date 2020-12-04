package com.grudus.adventofcode;


import io.vavr.collection.List;

import static io.vavr.collection.List.ofAll;

public class Launcher {
    public static void main(String[] args) {
        Day day = new Day04();
        List<String> input = ofAll(Utils.readFileInput(day.getClass()));

        System.out.println(day.firstStar(input));
        System.out.println(day.secondStar(input));
    }
}
