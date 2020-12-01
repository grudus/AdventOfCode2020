package com.grudus.adventofcode.day01;

import com.grudus.adventofcode.Utils;
import io.vavr.Tuple2;
import io.vavr.Tuple3;

import java.util.List;

import static io.vavr.collection.List.*;

//--- Day 1: Report Repair ---
public class Day01 {

    public static long firstStar(List<String> input) {
        return findProductOfSum(input, 2);
    }

    public static long secondStar(List<String> input) {
        return findProductOfSum(input, 3);
    }


    public static long findProductOfSum(List<String> expenseReport, int numberOfEntriesToSum) {
        var list = ofAll(expenseReport).map(Long::valueOf);

        return range(0, numberOfEntriesToSum - 1)
                .map(i -> list)
                .foldLeft(list.map(x -> ofAll(x)), (acc, singleList) -> acc.flatMap(xs -> singleList.map(xs::append)))
                .toStream()
                .find(itemList -> itemList.sum().longValue() == 2020L)
                .map(itemList -> itemList.product().longValue())
                .getOrNull();
    }

    public static void main(String[] args) {
        var input = Utils.readFileInput(Day01.class);

        System.out.println(firstStar(input));
        System.out.println(secondStar(input));
    }
}

