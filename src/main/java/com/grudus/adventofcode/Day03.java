package com.grudus.adventofcode;

import io.vavr.collection.List;
import io.vavr.collection.Stream;

public class Day03 extends Day<Long> {

    @Override
    public Long firstStar(List<String> input) {
        return Long.valueOf(countTreesInForest(input, new Slope(3, 1)));
    }

    @Override
    public Long secondStar(List<String> input) {
        return List.of(new Slope(1, 1), new Slope(3, 1), new Slope(5, 1), new Slope(7, 1), new Slope(1, 2))
                .map(slope -> countTreesInForest(input, slope))
                .product()
                .longValue();
    }

    private Integer countTreesInForest(List<String> forest, Slope slope) {
        int forestSizeX = forest.get(0).length();
        int forestSizeY = forest.size();

        return Stream.iterate(new Coordinate(0, 0),
                previousCoord -> {
                    Coordinate nextCoord = previousCoord.go(slope);
                    return nextCoord.x >= forestSizeX ? nextCoord.goX(-forestSizeX) : nextCoord;
                })
                .takeWhile(coord -> coord.y < forestSizeY)
                .count(coord -> forest.get(coord.y).charAt(coord.x) == '#');
    }


    record Slope(int dx, int dy) {
    }

    record Coordinate(int x, int y) {
        public Coordinate go(Slope slope) {
            return new Coordinate(x + slope.dx, y + slope.dy);
        }

        public Coordinate goX(int dx) {
            return new Coordinate(x + dx, y);
        }
    }
}
