// COVID-19 Model - Antigen Test twice
dtmc

const double p;
const double r;
const double ss;
const double t;



module die

	// local state
	s : [0..101] init 0;
	// value of the COVID-19
	C : [0..1] init 0;
  	// value of the Symptoms
        S : [0..1] init 0;
  	// value of the Antigen Test
        A1 : [0..1] init 0;
  	// value of the Antigen Test 2
        A2 : [0..1] init 0;

	[] s=0 -> 0.05 : (s'=1) + 0.95 : (s'=2);
	[] s=1 -> 0.698 : (s'=3) + 0.302 : (s'=4);
	[] s=2 -> 0.1 : (s'=5) + 0.9 : (s'=6);
	[] s=3 -> p : (s'=7) + 1-p : (s'=0);
	[] s=4 -> r : (s'=8) + 1-r : (s'=0);
	[] s=5 -> ss : (s'=9) + 1-ss : (s'=0);
	[] s=6 -> t : (s'=10) + 1-t : (s'=0);
        [] s=7 -> p : (s'=11) + 1-p : (s'=0);
        [] s=77 -> p : (s'=11) + 1-p : (s'=0);
        [] s=8 -> r : (s'=11) + 1-r : (s'=0);
        [] s=88 -> r : (s'=11) + 1-r : (s'=0);
        [] s=9 -> ss : (s'=13) + 1-ss : (s'=0);
        [] s=99 -> ss : (s'=13) + 1-ss : (s'=0);
        [] s=10 -> t : (s'=13) + 1-t : (s'=0);
        [] s=101 -> t : (s'=13) + 1-t : (s'=0);
	[] s=11 -> 1 : (s'=11);
        [] s=12 -> 1 : (s'=12);
        [] s=13 -> 1 : (s'=15);
        [] s=14 -> 1 : (s'=14);
        [] s=15 -> 1 : (s'=15);





	
endmodule

rewards "test"
	[] s<7 : 1;
endrewards

label "covidYgivenANAN" = s=13;
