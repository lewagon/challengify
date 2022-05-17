
// $WIPE_BEGIN
document.querySelector('#solo-scoreboard~* thead tr')
.insertAdjacentHTML("beforeend", '<th class="w-3/12 font-light">&nbsp;Abs&nbsp;</th><th class="w-3/12 font-light">&nbsp;Rel&nbsp;</th>')
// $WIPE_END

const u = document.querySelector("#user-rank > td:last-child");
const userScore = u.innerText;

let prevScore = 0;
let prevLine = null;
[...document.querySelectorAll('#solo-scoreboard~* tbody tr')]
.forEach(e => {
    // $CHA_BEGIN
    s = e.querySelector(':scope > td:last-child')
    score = s.innerText
    if (s != u) {
        e.insertAdjacentHTML("beforeend", `<td py-1 strong text-lg>${score - userScore}</td>`);
    } else {
        e.insertAdjacentHTML("beforeend", `<td py-1 strong text-lg><img class="w-5 h-5 ml-2" src="/packs/media/images/parrot-58d4bcc53c62eccd4e7120cda0986c4a.gif"></td>`);
    }
    if (prevLine != null) {
        prevLine.insertAdjacentHTML("beforeend", `<td py-1 strong text-lg>+${prevScore - score}</td>`);
    }
    prevScore = score
    prevLine = e
    // $CHA_END
});
