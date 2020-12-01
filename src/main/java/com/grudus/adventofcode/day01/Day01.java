package com.grudus.adventofcode.day01;

import com.google.common.collect.Lists;
import com.grudus.adventofcode.Utils;
import io.vavr.collection.List;

import static io.vavr.collection.List.ofAll;
import static io.vavr.collection.List.range;

//--- Day 1: Report Repair ---
public class Day01 {

    public static long firstStar(List<Long> expenseReport) {
        return findProductOfSum(expenseReport, 2);
    }

    public static long secondStar(List<Long> expenseReport) {
        return findProductOfSum(expenseReport, 3);
    }


    public static long findProductOfSum(List<Long> expenseReport, int numberOfEntriesToSum) {
        var lists = range(0, numberOfEntriesToSum).map(i -> expenseReport.toJavaList()).toJavaList();
        var combinations = Lists.cartesianProduct(lists);

        return ofAll(combinations)
                .toStream()
                .map(List::ofAll)
                .find(itemList -> itemList.sum().longValue() == 2020)
                .map(itemList -> itemList.product().longValue())
                .getOrElse(0L);
    }

    public static void main(String[] args) {
        var input = Utils.readFileInput(Day01.class);
        var expenseReport = ofAll(input).map(Long::valueOf);

        System.out.println(firstStar(expenseReport));
        System.out.println(secondStar(expenseReport));
    }
}

