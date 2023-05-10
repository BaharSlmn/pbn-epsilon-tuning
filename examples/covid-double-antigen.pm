// COVID-19 Model - Antigen Test twice
dtmc

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
	[] s=3 -> 0.72 : (s'=7) + 0.28 : (s'=77);
	[] s=4 -> 0.58 : (s'=8) + 0.42 : (s'=88);
	[] s=5 -> 0.005 : (s'=9) + 0.995 : (s'=99);
	[] s=6 -> 0.01 : (s'=10) + 0.99 : (s'=101);
        [] s=7 -> 0.72 : (s'=11) + 0.28 : (s'=12);
        [] s=77 -> 0.72 : (s'=11) + 0.28 : (s'=12);
        [] s=8 -> 0.58 : (s'=11) + 0.42 : (s'=12);
        [] s=88 -> 0.58 : (s'=11) + 0.42 : (s'=12);
        [] s=9 -> 0.005 : (s'=11) + 0.995 : (s'=12);
        [] s=99 -> 0.005 : (s'=11) + 0.995 : (s'=12);
        [] s=10 -> 0.01 : (s'=11) + 0.99 : (s'=12);
        [] s=101 -> 0.01 : (s'=11) + 0.99 : (s'=12);
	[] s=11 -> 1 : (s'=11);
        [] s=12 -> 1 : (s'=12);



	
endmodule

rewards "test"
	[] s<7 : 1;
endrewards

label "covidYgivenANAN" = s=11;
label "A2P" = s=11;
