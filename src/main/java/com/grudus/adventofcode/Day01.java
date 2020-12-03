package com.grudus.adventofcode;

import com.google.common.collect.Lists;
import io.vavr.collection.List;

import static io.vavr.collection.List.ofAll;
import static io.vavr.collection.List.range;

//--- Day 1: Report Repair ---
public class Day01 extends Day<Long> {

    public Long firstStar(List<String> expenseReport) {
        return findProductOfSum(expenseReport.map(Long::parseLong), 2);
    }

    public Long secondStar(List<String> expenseReport) {
        return findProductOfSum(expenseReport.map(Long::parseLong), 3);
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
}

