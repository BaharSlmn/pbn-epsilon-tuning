// COVID-19 Model - PCR Test and Antigen Test
dtmc



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
	[] s=3 -> 0.72 : (s'=7) + 0.28 : (s'=0);
	[] s=4 -> 0.58 : (s'=7) + 0.42 : (s'=0);
	[] s=5 -> 0.005 : (s'=8) + 0.995 : (s'=0);
	[] s=6 -> 0.01 : (s'=8) + 0.99 : (s'=0);
        [] s=7 -> 0.95 : (s'=9) + 0.05 : (s'=0);
        [] s=8 -> 0.04 : (s'=10) + 0.96 : (s'=0);
	[] s=10 -> 1: (s'=10);
	[] s=10 -> 1: (s'=10);
	
endmodule

rewards "test"
	[] s<7 : 1;
endrewards

label "covidYgivenantiNpcrN" = s=10;
