// COVID-19 Model - PCR Test and Antigen Test
dtmc

const double p;
const double q;
const double r;
const double ss;
const double t;


module die

	// local state
	s : [0..10] init 0;
	// value of the COVID-19
	C : [0..1] init 0;
  	// value of the Symptoms
        S : [0..1] init 0;
  	// value of the Antigen Test
        A : [0..1] init 0;
  	// value of the PCR Test
        P : [0..1] init 0;

	[] s=0 -> 0.05 : (s'=1) + 0.95 : (s'=2);
	[] s=1 -> 0.698 : (s'=3) + 0.302 : (s'=4);
	[] s=2 -> 0.1 : (s'=5) + 0.9 : (s'=6);
	[] s=3 -> p : (s'=7) + (1-p) : (s'=0);
	[] s=4 -> r : (s'=7) + (1-r) : (s'=0);
	[] s=5 -> ss : (s'=8) + (1-ss) : (s'=0);
	[] s=6 -> t : (s'=8) + (1-t) : (s'=0);
        [] s=7 -> q : (s'=9) + (1-q) : (s'=0);
        [] s=8 -> (4*t) : (s'=10) + (1-(4*t)) : (s'=0);
	[] s=10 -> 1: (s'=10);
	[] s=10 -> 1: (s'=10);
	
endmodule

rewards "test"
	[] s<7 : 1;
endrewards

label "covidYgivenantiNpcrN" = s=10;
