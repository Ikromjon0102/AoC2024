
# part one
def can_construct(design, patterns, memo={}):
    # Base case: if the design is empty, it can be constructed
    if not design:
        return True

    # Check if this design is already memoized
    if design in memo:
        return memo[design]

    # Try to use each pattern to construct the design
    for pattern in patterns:
        if design.startswith(pattern):  # If the design starts with this pattern
            if can_construct(design[len(pattern):], patterns, memo):
                memo[design] = True
                return True

    # If no pattern can construct the design
    memo[design] = False
    return False


def count_possible_designs(towel_patterns, designs):
    patterns = towel_patterns.split(', ')
    count = 0
    for design in designs:
        if can_construct(design, patterns):
            count += 1
    return count

# Input data
towel_patterns = "grg, rwguw, bbw, gbrruug, ubbbbw, bggwu, gwbwbb, urwbrwr, wwww, rwbubwr, wrggb, ruuw, gub, wgbr, gur, gugw, gwbbg, rrg, gbgrbbbb, ugu, rrbbgruu, urub, rwuw, brrw, rwr, ugbbbbb, uwr, rgbbw, rgrgg, bwwgw, rg, ur, wgrrr, rbubgu, gwu, uwrgb, brb, rgrgrw, brggu, bbrubuwg, uwgrrbug, bwwbrrrb, ruuwgr, guw, gbr, guwu, uuubbuwb, guu, g, grbwb, gggbbbu, ugugw, wwg, wggr, bwr, wwr, ubuwbbw, gwwr, gugbuww, rwb, ugbb, bwbwwuw, bbr, rgb, ruu, ubbb, bwrgurgb, rubg, rggb, rbuwb, uguurb, gwrw, wwuwr, rrur, grwggw, bgwr, rgugb, wbg, wwb, wr, wbur, ugbbr, wgwurru, ug, ggbwgg, bwu, wuug, gwbwr, bbbbgrr, bw, ubbg, urwuw, uwrrbgw, bwwwr, wgrwww, wg, burwbu, gurrrru, ugub, gwrrg, ubrw, gruwrw, ubr, gbbb, gbu, rbu, ggw, rrgbb, wuubbw, wggbuur, uuw, urg, wbuu, uruug, wrw, wurgbw, gbgbgb, gwb, bwb, bwug, ggub, uug, bww, grr, uurrr, uw, ubb, bgrg, rgbbr, rrb, rr, bgr, bugrbg, bgubur, ggbb, bub, gwruuw, rbg, uuuwbbr, wgr, rbuurrw, bwuwwb, ugb, gbgr, gubu, bgb, uguru, uwg, wgwwugrg, gwwrb, wgu, rru, rwbbwg, gwwuur, ggwgwrr, uwbr, uuu, wbb, wggg, buu, rbuggb, wuuggg, urgg, u, ww, uuwuub, gr, rbgbb, bwburuw, rug, bubwb, wb, wgw, brr, wgrrw, urr, gu, bbrw, grbb, uwgwu, rrr, rwu, urw, gurrb, grw, bugub, rurrww, wrwuugr, wgggrr, brrgguu, rgww, wgg, wuwwwuw, ubruwuwr, brgw, wbu, rgw, uwgurg, rgrb, rrw, ubwggr, uruw, uru, urwgb, gw, bgrbuu, gbrrwwru, gbrgr, bbbgbrgb, bgg, rww, urbggb, wgrr, bbrrww, gb, rbbb, gbbrrw, rubwb, wrbrwrww, ubuuw, bgbww, rgg, rbww, rwgu, uwrw, uwrr, gggr, wbbgrwbg, uggrggub, uww, wu, wuu, uwbbur, ggww, bubwr, rgwb, bwg, gugr, burgw, rgur, wrbg, rwrgrr, gug, wbbuw, bbg, guwub, uruu, gurg, ruw, rbrbgrrw, bwurg, gwww, gbbu, ggu, wgwbw, guuww, uwbbrbr, bggbuu, rbrg, rwww, bbubb, ubg, rurbb, ugugwrb, wrg, wubwu, uubw, r, gbuuuu, ugrgg, rgu, rwwr, gbgu, ugwwrg, ru, bwbbbgu, bug, ugg, rwwwrwb, rgwgbr, rugbguub, rwub, uugrbw, rbr, rbb, wwguw, bb, ubuwr, ggbwrb, ubu, bwgb, ugw, rwrrgw, bbrrg, wgbggw, rrwuwrwu, urgggr, gwwggw, bu, wbw, rggrb, wbrru, brw, gww, gwg, ubuuuw, wwrg, wwuwrug, grwgrb, gbb, uwwb, wbgr, wwwwg, rugr, bwrb, gg, ubggg, gbrwru, brbr, ub, gbrbug, gguwurw, bggr, bbb, wubbbu, wub, brgbwb, wbrbg, wwrw, bgw, uwwg, rrrrgw, uwb, urubg, gwr, wrgrg, ggr, wbubbu, uwu, bgrbb, ggbg, brg, rwwrb, uwug, bwwww, grb, wgwrwgb, wgrbbr, wrr, rwwwr, gwwwu, buw, gbw, wug, wugw, wuw, ggbww, wrggrbw, wru, wwrguwu, wwbb, bguw, wrbb, rub, rbbr, gwuw, gbbggb, rw, gwgb, wrubbb, wbgur, bwbwbgg, rgbb, wbrr, www, bgbg, ubwg, wrggggr, wgbuug, gwub, buubuug, brbb, ggugwbu, rguwb, bgu, gubuurgb, bgub, uwbbrg, gbru, wwu, grbgbbw, rbw, ggg, wrb, rb, wbwgrurw, wgrgu, wgb, uuubrwg, gwgu, wubww, guubw, rgggrwb, uurw, w, rbuu, ugwwu, buwwubg, ubgrgb, ugr, uggwbru, ggb, bbu, rur, wuuuwbu, gru, rbgwu, ugbwbgr, ggrrb, rgr, rugg, uu, ugrgb, wbr, gguwrrwb, rbrgg, wgbwwg, uur, ggbr, rrww, bur, wuwgur, urbb, uugr, ugwr, ubrgu, wbgggg, uugrb, bgggr, rwg, bwgw, wbwg, uwgbb, wrwu, gbg, ggrbu, rwubr"
designs = [i.strip('\n') for i in open('input.txt', 'r').readlines()]

# Count the possible designs
possible_count = count_possible_designs(towel_patterns, designs)
print(f"Number of possible designs: {possible_count}")




def count_ways_to_construct(design, patterns, memo={}):
    # Base case: if the design is empty, there's one way (do nothing)
    if not design:
        return 1

    # Check if the result is already memoized
    if design in memo:
        return memo[design]

    # Initialize the count of ways
    ways = 0

    # Try to use each pattern
    for pattern in patterns:
        if design.startswith(pattern):  # If the design starts with this pattern
            # Recur for the remaining part of the design
            ways += count_ways_to_construct(design[len(pattern):], patterns, memo)

    # Memoize and return the result
    memo[design] = ways
    return ways


def total_arrangements(towel_patterns, designs):
    patterns = towel_patterns.split(', ')
    total = 0
    for design in designs:
        total += count_ways_to_construct(design, patterns)
    return total


# Input data
towel_patterns = "grg, rwguw, bbw, gbrruug, ubbbbw, bggwu, gwbwbb, urwbrwr, wwww, rwbubwr, wrggb, ruuw, gub, wgbr, gur, gugw, gwbbg, rrg, gbgrbbbb, ugu, rrbbgruu, urub, rwuw, brrw, rwr, ugbbbbb, uwr, rgbbw, rgrgg, bwwgw, rg, ur, wgrrr, rbubgu, gwu, uwrgb, brb, rgrgrw, brggu, bbrubuwg, uwgrrbug, bwwbrrrb, ruuwgr, guw, gbr, guwu, uuubbuwb, guu, g, grbwb, gggbbbu, ugugw, wwg, wggr, bwr, wwr, ubuwbbw, gwwr, gugbuww, rwb, ugbb, bwbwwuw, bbr, rgb, ruu, ubbb, bwrgurgb, rubg, rggb, rbuwb, uguurb, gwrw, wwuwr, rrur, grwggw, bgwr, rgugb, wbg, wwb, wr, wbur, ugbbr, wgwurru, ug, ggbwgg, bwu, wuug, gwbwr, bbbbgrr, bw, ubbg, urwuw, uwrrbgw, bwwwr, wgrwww, wg, burwbu, gurrrru, ugub, gwrrg, ubrw, gruwrw, ubr, gbbb, gbu, rbu, ggw, rrgbb, wuubbw, wggbuur, uuw, urg, wbuu, uruug, wrw, wurgbw, gbgbgb, gwb, bwb, bwug, ggub, uug, bww, grr, uurrr, uw, ubb, bgrg, rgbbr, rrb, rr, bgr, bugrbg, bgubur, ggbb, bub, gwruuw, rbg, uuuwbbr, wgr, rbuurrw, bwuwwb, ugb, gbgr, gubu, bgb, uguru, uwg, wgwwugrg, gwwrb, wgu, rru, rwbbwg, gwwuur, ggwgwrr, uwbr, uuu, wbb, wggg, buu, rbuggb, wuuggg, urgg, u, ww, uuwuub, gr, rbgbb, bwburuw, rug, bubwb, wb, wgw, brr, wgrrw, urr, gu, bbrw, grbb, uwgwu, rrr, rwu, urw, gurrb, grw, bugub, rurrww, wrwuugr, wgggrr, brrgguu, rgww, wgg, wuwwwuw, ubruwuwr, brgw, wbu, rgw, uwgurg, rgrb, rrw, ubwggr, uruw, uru, urwgb, gw, bgrbuu, gbrrwwru, gbrgr, bbbgbrgb, bgg, rww, urbggb, wgrr, bbrrww, gb, rbbb, gbbrrw, rubwb, wrbrwrww, ubuuw, bgbww, rgg, rbww, rwgu, uwrw, uwrr, gggr, wbbgrwbg, uggrggub, uww, wu, wuu, uwbbur, ggww, bubwr, rgwb, bwg, gugr, burgw, rgur, wrbg, rwrgrr, gug, wbbuw, bbg, guwub, uruu, gurg, ruw, rbrbgrrw, bwurg, gwww, gbbu, ggu, wgwbw, guuww, uwbbrbr, bggbuu, rbrg, rwww, bbubb, ubg, rurbb, ugugwrb, wrg, wubwu, uubw, r, gbuuuu, ugrgg, rgu, rwwr, gbgu, ugwwrg, ru, bwbbbgu, bug, ugg, rwwwrwb, rgwgbr, rugbguub, rwub, uugrbw, rbr, rbb, wwguw, bb, ubuwr, ggbwrb, ubu, bwgb, ugw, rwrrgw, bbrrg, wgbggw, rrwuwrwu, urgggr, gwwggw, bu, wbw, rggrb, wbrru, brw, gww, gwg, ubuuuw, wwrg, wwuwrug, grwgrb, gbb, uwwb, wbgr, wwwwg, rugr, bwrb, gg, ubggg, gbrwru, brbr, ub, gbrbug, gguwurw, bggr, bbb, wubbbu, wub, brgbwb, wbrbg, wwrw, bgw, uwwg, rrrrgw, uwb, urubg, gwr, wrgrg, ggr, wbubbu, uwu, bgrbb, ggbg, brg, rwwrb, uwug, bwwww, grb, wgwrwgb, wgrbbr, wrr, rwwwr, gwwwu, buw, gbw, wug, wugw, wuw, ggbww, wrggrbw, wru, wwrguwu, wwbb, bguw, wrbb, rub, rbbr, gwuw, gbbggb, rw, gwgb, wrubbb, wbgur, bwbwbgg, rgbb, wbrr, www, bgbg, ubwg, wrggggr, wgbuug, gwub, buubuug, brbb, ggugwbu, rguwb, bgu, gubuurgb, bgub, uwbbrg, gbru, wwu, grbgbbw, rbw, ggg, wrb, rb, wbwgrurw, wgrgu, wgb, uuubrwg, gwgu, wubww, guubw, rgggrwb, uurw, w, rbuu, ugwwu, buwwubg, ubgrgb, ugr, uggwbru, ggb, bbu, rur, wuuuwbu, gru, rbgwu, ugbwbgr, ggrrb, rgr, rugg, uu, ugrgb, wbr, gguwrrwb, rbrgg, wgbwwg, uur, ggbr, rrww, bur, wuwgur, urbb, uugr, ugwr, ubrgu, wbgggg, uugrb, bgggr, rwg, bwgw, wbwg, uwgbb, wrwu, gbg, ggrbu, rwubr"
designs = [i.strip('\n') for i in open('input.txt', 'r').readlines()]

total_ways = total_arrangements(towel_patterns, designs)
print(f"Total number of arrangements: {total_ways}")