package com.grudus.adventofcode.day01;

import com.grudus.adventofcode.Utils;
import io.vavr.Tuple2;
import io.vavr.Tuple3;

import java.util.List;

import static io.vavr.collection.List.ofAll;

//--- Day 1: Report Repair ---
public class Day01 {

    public static long firstStar(List<String> input) {
        var list = ofAll(input).map(Long::valueOf);

        return list
                .flatMap(first -> list.map(elem -> new Tuple2<>(first, elem)))
                .toStream()
                .find(pair -> pair._1 + pair._2 == 2020)
                .map(pair -> pair._1 * pair._2)
                .getOrNull();

    }

    public static long secondStar(List<String> input) {
        var list = ofAll(input).map(Long::valueOf);

        return list
                .flatMap(first -> list.flatMap(second -> list.map(third -> new Tuple3<>(first, second, third))))
                .toStream()
                .find(pair -> pair._1 + pair._2 + pair._3 == 2020)
                .map(pair -> pair._1 * pair._2 * pair._3)
                .getOrNull();

    }

    public static void main(String[] args) {
        var input = Utils.readFileInput(Day01.class);

        System.out.println(firstStar(input));
        System.out.println(secondStar(input));
    }
}

