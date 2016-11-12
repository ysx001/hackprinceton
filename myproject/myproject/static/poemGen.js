/**
 * Created by Son Pham on 11/12/2016.
 */

// Poem Generator JavaScript
// Keith Enevoldsen, thinkzone.wlonk.com

random_count=0;
nsentences=0;
nwords1=0; nwords2=0; nwords3=0; nwords4=0; nwords5=0;
nwords6=0; nwords7=0; nwords8=0; nwords9=0;

function generate_input(form, sample_name)
{
  form.title1.value = "Concrete Nouns";
  form.title2.value = "Abstract Nouns";
  form.title3.value = "Transitive Verbs";
  form.title4.value = "Intransitive Verbs";
  form.title5.value = "Adjectives";
  form.title6.value = "Adverbs";
  form.title7.value = "";
  form.title8.value = "";
  form.title9.value = "Interjections";
  form.sentences.value =
    "The 5 1 6 3s the 1."
    +"\n5, 5 1s 6 3 a 5, 5 1."
    +"\n2 is a 5 1."
    +"\n9, 2!"
    +"\n1s 4!"
    +"\nThe 1 4s like a 5 1."
    +"\n1s 4 like 5 1s."
    +"\nWhy does the 1 4?"
    +"\n4 6 like a 5 1."
    +"\n2, 2, and 2."
    +"\nWhere is the 5 1?"
    +"\nAll 1s 3 5, 5 1s."
    +"\nNever 3 a 1."
  ;
  if (sample_name == "Sea") {
    form.list1.value = "sea\nship\nsail\nwind\nbreeze\nwave\ncloud\nmast\ncaptain\nsailor\nshark\nwhale\ntuna\nseashell\npirate\nlad\ngirl\ngull\nreef\nshore\nmainland\nmoon\nsun";
    form.list2.value = "adventure\ncourage\nendurance\ndesolation\ndeath\nlife\nlove\nfaith";
    form.list3.value = "command\nview\nlead\npull\nlove\ndesire\nfight";
    form.list4.value = "travel\nsail\nwave\ngrow\nrise\nfall\nendure\ndie";
    form.list5.value = "big\nsmall\nold\ncold\nwarm\nsunny\nrainy\nmisty\nclear\nstormy\nrough\nlively\ndead";
    form.list6.value = "swiftly\ncalmly\nquietly\nroughly";
    form.list7.value = "";
    form.list8.value = "";
    form.list9.value = "o\noh\nooh\nah\nlord\ngod\nwow\ngolly gosh";
  } else if (sample_name == "City") {
    form.list1.value = "street\nsidewalk\ncorner\ndoor\nwindow\nhood\nslum\nskyscraper\ncar\ntruck\nguy\ngirl\njob\nflower\nlight\ncigarette\nrain\njackhammer\ndriver\nworker";
    form.list2.value = "action\nwork\nnoise\ndesolation\ndeath\nlife\nlove\nfaith\nanger\nexhaustion";
    form.list3.value = "get\ngrab\nshove\nlove\ndesire\nbuy\nsell\nfight\nhustle\ndrive";
    form.list4.value = "talk\ngab\nwalk\nrun\nstop\neat\ngrow\nshrink\nshop\nwork";
    form.list5.value = "big\nsmall\nold\nfast\ncold\nhot\ndark\ndusty\ngrimy\ndry\nrainy\nmisty\nnoisy\nfaceless\ndead";
    form.list6.value = "quickly\nloudly\ncalmly\nquietly\nroughly";
    form.list7.value = "";
    form.list8.value = "";
    form.list9.value = "o\noh\nooh\nah\nlord\ngod\ndamn";
  } else {
    clear_all(form);
  }
  form.outtext.value = "";
  count_all_lines(form);
}

function clear_all(form)
{
  form.Samples.value = "-";
  form.title1.value = "";
  form.title2.value = "";
  form.title3.value = "";
  form.title4.value = "";
  form.title5.value = "";
  form.title6.value = "";
  form.title7.value = "";
  form.title8.value = "";
  form.title9.value = "";
  form.list1.value = "";
  form.list2.value = "";
  form.list3.value = "";
  form.list4.value = "";
  form.list5.value = "";
  form.list6.value = "";
  form.list7.value = "";
  form.list8.value = "";
  form.list9.value = "";
  form.sentences.value = "";
  form.outtext.value = "";
  count_all_lines(form);
}

function count_all_lines(form)
{
  nwords1 = count_lines(form.list1);
  nwords2 = count_lines(form.list2);
  nwords3 = count_lines(form.list3);
  nwords4 = count_lines(form.list4);
  nwords5 = count_lines(form.list5);
  nwords6 = count_lines(form.list6);
  nwords7 = count_lines(form.list7);
  nwords8 = count_lines(form.list8);
  nwords9 = count_lines(form.list9);
  nsentences = count_lines(form.sentences);
}

function random(maxnum)
{
  r = Math.floor(Math.random() * maxnum) + 1;
  if (r > maxnum) r = maxnum;
  return r;
}

function count_lines(txt)
{
  str = txt.value;
  len = str.length;
  nword = 1;
  for (i = 0; i < len; i++) {
    if (str.charAt(i) == "\n") {
      nword++;
    }
  }
  if (str.charAt(len-1) == "\n") nword--;
  return nword;
}

function get_line(str, lnum)
{
  len = str.length;
  iline = 1; ichar = 0; jchar = -1;
  for (i = 0; i < len; i++) {
    if (str.charAt(i) == "\n") {
      iline++;
      if (iline == lnum) {
        ichar = i + 1;
      } else if (iline == (lnum + 1)) {
        jchar = i - 1;
        if (str.charAt(jchar) == "\r") {
          jchar--;
        }
        break;
      }
    }
  }
  if (jchar < 0) jchar = len - 1;
// Note: Use loop because substr() doesn't work consistently on old browsers
  s = "";
  for (i = ichar; i <= jchar; i++) {
    s = s + str.charAt(i);
  }
  return s;
}

function initial_cap(str)
{
// Note: Use loop because substr() doesn't work consistently on old browsers
  len = str.length;
  s = "";
  for (i = 0; i <= len; i++) {
    if (i == 0) {
      s = s + str.charAt(i).toUpperCase();
    } else {
      s = s + str.charAt(i);
    }
  }
  return s;
}

function make_poem(form)
{
  form.outtext.value = "";
  count_all_lines(form);
  nlines = random(4) + 1;
  for (ilin = 1; ilin <= nlines; ilin++) {
    make_poem_line(form)
  }
}

function make_poem_line(form)
{
  pattern = get_line(form.sentences.value, random(nsentences));
  lenpat = pattern.length;
  for (ichr = 0; ichr < lenpat; ichr++) {
    chr = pattern.charAt(ichr);
    // If the pattern contains a digit n, then pick a random word from list n
    if ((chr >= '1') && (chr <= '9')) {
      if (chr == '1') {
        wrd = get_line(form.list1.value, random(nwords1));
      } else if (chr == '2') {
        wrd = get_line(form.list2.value, random(nwords2));
      } else if (chr == '3') {
        wrd = get_line(form.list3.value, random(nwords3));
      } else if (chr == '4') {
        wrd = get_line(form.list4.value, random(nwords4));
      } else if (chr == '5') {
        wrd = get_line(form.list5.value, random(nwords5));
      } else if (chr == '6') {
        wrd = get_line(form.list6.value, random(nwords6));
      } else if (chr == '7') {
        wrd = get_line(form.list7.value, random(nwords7));
      } else if (chr == '8') {
        wrd = get_line(form.list8.value, random(nwords8));
      } else if (chr == '9') {
        wrd = get_line(form.list9.value, random(nwords9));
      } else {
        wrd = '';
      }
      // Capitalize first letter of sentence
      if (ichr == 0) {
        wrd = initial_cap(wrd);
      }
      form.outtext.value = form.outtext.value + wrd;
    } else {
      form.outtext.value = form.outtext.value + chr;
    }
  }
  form.outtext.value = form.outtext.value + "\n";
}

//////////////////////////////////////////
// make_poem
//////////////////////////////////////////

function create_form() {
  var form = {}
  form.title1 = {}; form.title1.value = "";
  form.title2 = {}; form.title2.value = "";
  form.title3 = {}; form.title3.value = "";
  form.title4 = {}; form.title4.value = "";
  form.title5 = {}; form.title5.value = "";
  form.title6 = {}; form.title6.value = "";
  form.title7 = {}; form.title7.value = "";
  form.title8 = {}; form.title8.value = "";
  form.title9 = {}; form.title9.value = "";
  form.sentences = {}; form.sentences.value = "";
  form.list1 = {}; form.list1.value = "";
  form.list2 = {}; form.list2.value = "";
  form.list3 = {}; form.list3.value = "";
  form.list4 = {}; form.list4.value = "";
  form.list5 = {}; form.list5.value = "";
  form.list6 = {}; form.list6.value = "";
  form.list7 = {}; form.list7.value = "";
  form.list8 = {}; form.list8.value = "";
  form.list9 = {}; form.list9.value = "";
  form.outtext = {}; form.outtext.value = "";
  return form;
}

var form = create_form();
console.log(form)
var sample_name = "City";
generate_input(form, sample_name);
make_poem(form);
console.log(form.outtext.value);