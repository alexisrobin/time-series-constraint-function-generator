:-module(seed, [
	seed/5,
	seed_template/5,
	seed_glue_matrix/2
	]).

:-use_module(library(clpfd)).
:-use_module(tables).

/*
provides two interfaces, which enumerate the different seed automata
*/

/*
seed(Name,Before-After,InitialState, States, Links)
Name atom
Before, After are integers
InitialState atom
States is a list of atoms
Links is a list of terms arc(From,Sig,To,Letter)
From, To are state names
Sig is one of lt, gt, eq, geq, leq, neq
    (geq, leq and neq denote two links, really)
Letter is one of out, 
                 out(r),
                 out(a),
                 maybe(b), 
                 maybe(a), 
                 found_end, 
                 found, 
                 in
*/
seed(Name,BeforeAfter,Start,States,Updates):-
        seed_template(Name,Start,ExtendedStates,ExtendedUpdates,_),
%       write(Name),nl,
        pattern_table(Name,_,BeforeAfter,_),
%       write(Name-BeforeAfter-ExtendedStates),nl,
        extract_states(ExtendedStates,States),
%       write(States),nl,
        extract_updates(ExtendedUpdates,Updates).

extract_states([],[]).
extract_states([return(_)|R],S):-
        !,
        extract_states(R,S).
extract_states([return(_,_)|R],S):-
        !,
        extract_states(R,S).
extract_states([state(S,_)|R1],[S|S1]):-
        !,
        extract_states(R1,S1).
extract_states([R|_],_):-
        write(missing_case(R)),
        abort.

extract_updates([],[]).
extract_updates([S|S1],[R|R1]):-
        extract_update(S,R),
        extract_updates(S1,R1).

% argument 5 is the placement of the arc
% argument 6 is the optional placement of the arc label
extract_update(arc(From,Op,To,Seed),arc(From,Op,To,Seed)):-!.
extract_update(arc(From,Op,To,Seed,_),arc(From,Op,To,Seed)):-!.
extract_update(arc(From,Op,To,Seed,_,_),arc(From,Op,To,Seed)):-!.

/*
seed_template(name,starting state,states,links,node distance)
states is a list of terms state(name,property) or 
                          return(node decor[,node decor])
links is a list of terms arc(from,sig,to,letter[,link decoration][,label decor])
arc link decoration can be 
no_show = do not show arc in figure
no_update = do not show variable updates in figure
'' nothing is applied
tikz code like 'loop above' or 'bend left'

arc label decoration decribes the placement of the link label
this should be tikz code including sloped (label follows the direction
 of arc) which is not applied if no variable updates are shown
*/
seed_template(bump_on_decreasing_sequence, s, 
              [state(s,initial(left)),
	       state(r,'right of=s'),
	       state(t,'right of=r'),
	       state(u,at('4.5,-6.2')),
	       state(v,at('4.5,-2.5')),
               return(at(5.5,-1))],
              [arc(s,leq,s,out,'loop above'),
	       arc(s,gt,r,out,'bend angle=10,bend left'),
	       arc(r,leq,s,out,'bend angle=10,bend left'),
	       arc(r,gt,t,out),
	       arc(t,gt,t,out,'loop above'),
	       arc(t,eq,s,out,'bend angle=35,bend right','above=1pt'),
	       arc(t,lt,u,maybe(b),'','below=2pt,sloped,pos=0.7'),
	       arc(u,leq,s,out(r),'','below=2pt,sloped'),
	       arc(u,gt,v,maybe(b),'','above=2pt,sloped,pos=0.55'),
	       arc(v,leq,s,out(r),'','below=2pt,sloped,pos=0.3'),
	       arc(v,gt,t,found_end, '','below=2pt,sloped,pos=0.35')],
	      48).

seed_template(decreasing, s, 
              [state(s,initial(above)),
               return(at(0,-1.5))], 
              [arc(s,gt,s,found_end,'loop left'),
               arc(s,leq,s,out,'loop right')],30).

seed_template(decreasing_sequence, s, 
              [state(s,initial(above)),
               state(t,'below of=s'),
               return(at('$(s)!0.5!(t)$'),'rotate=90')], 
              [arc(s,gt,t,found,'bend left'),
               arc(s,leq,s,out,'loop right'),
               arc(t,gt,t,in,'loop right'),
               arc(t,eq,t,maybe(a),'loop left'),
               arc(t,lt,s,out(a),'bend left')],30).

seed_template(decreasing_terrace, s, 
              [state(s,initial(left)),
               state(r,'below of=s'),
               state(t,at('$(r)-(5,0)$')),
               return(at(-2,-1.5))], 
              [arc(s,leq,s,out,'loop right'),
	       arc(s,gt,r,out,'','left=0.5,sloped'),
               arc(r,gt,r,out,'loop right'),
               arc(r,eq,t,maybe(b),'above'),
               arc(r,lt,s,out,'bend angle=20,bend right','right=2'),
               arc(t,eq,t,maybe(b),'loop left'),
               arc(t,gt,r,found_end,'bend angle=18,bend right','left=2,below,sloped'),
               arc(t,lt,s,out(r),'bend angle=20,bend left','left=2,above,sloped')],
              32).

seed_template(dip_on_increasing_sequence, s, 
              [state(s,initial(left)),
	       state(r,'right of=s'),
	       state(t,'right of=r'),
	       state(u,at('4.5,-6.2')),
	       state(v,at('4.5,-2.5')),
               return(at(5.5,-1))],
              [arc(s,geq,s,out,'loop above'),
	       arc(s,lt,r,out,'bend angle=10,bend left'),
	       arc(r,geq,s,out,'bend angle=10,bend left'),
	       arc(r,lt,t,out),
	       arc(t,lt,t,out,'loop above'),
	       arc(t,eq,s,out,'bend angle=35,bend right','above=1pt'),
	       arc(t,gt,u,maybe(b),'','below=2pt,sloped,pos=0.7'),
	       arc(u,geq,s,out(r),'','below=2pt,sloped'),
	       arc(u,lt,v,maybe(b),'','above=2pt,sloped,pos=0.55'),
	       arc(v,geq,s,out(r),'','below=2pt,sloped,pos=0.3'),
	       arc(v,lt,t,found_end, '','below=2pt,sloped,pos=0.35')],
	      48).

seed_template(gorge, s, 
              [state(s,initial(left)),
               state(r,'right of=s'),
               state(t,'below right of=r'),
               state(u,at('$(s)!0.4!(r)-(0,4.5)$')),
               return(at('$(s)!0.4!(r)-(0,0.4)$'))],
              [arc(s,leq,s,out,'loop above'),
               arc(s,gt,r,out,'bend angle=10,bend left'),
               arc(r,gt,r,maybe(b),'loop above'),
               arc(r,lt,t,found,'bend angle=10,bend left','very near start'),
               arc(r,eq,u,maybe(b),'bend angle=10,bend left','very near end'),
               arc(t,eq,t,maybe(a),'loop above','right'),
               arc(t,lt,t,in,'loop below','near start,right'),
               arc(t,gt,r,out(a),'bend angle=10,bend left','sloped,below=2pt,near start'),
               arc(u,eq,u,maybe(b),'loop below'),
%              arc(u,gt,r,maybe(b),'no_update','left=0.5,sloped'),
	       arc(u,gt,r,maybe(b),'bend angle=10,bend left','above=2,sloped'),
               arc(u,lt,s,out(r),'bend angle=10,bend left','left=2')],
              40).

seed_template(increasing, s, 
              [state(s,initial(above)),
               return(at(0,-1.5))], 
              [arc(s,geq,s,out,'loop right'),
               arc(s,lt,s,found_end,'loop left')],
              30).

seed_template(increasing_sequence, s,
              [state(s,initial(above)),
               state(t,'below of=s'),
               return(at('$(s)!0.5!(t)$'),'rotate=90')], 
              [arc(s,geq,s,out,'loop right'),
               arc(s,lt,t,found,'bend left'),
               arc(t,gt,s,out(a),'bend left'),
               arc(t,eq,t,maybe(a),'loop left'),
               arc(t,lt,t,in,'loop right')],
              30).

seed_template(increasing_terrace, s, 
              [state(s,initial(left)),
               state(r,'below of=s'),
               state(t,at('$(r)-(5,0)$')),
               return(at(-2,-1.5))], 
              [arc(s,geq,s,out,'loop right'),
               arc(s,lt,r,out,'','left=0.5,sloped'),
               arc(r,lt,r,out,'loop right'),
               arc(r,eq,t,maybe(b),'above'),
               arc(r,gt,s,out,'bend angle=20,bend right','right=2'),
               arc(t,eq,t,maybe(b),'loop left'),
	       arc(t,lt,r,found_end,'bend angle=18,bend right','left=2,below,sloped'),
               arc(t,gt,s,out(r),'bend angle=20,bend left','left=2,above,sloped')],
              32).

seed_template(inflexion, s,
              [state(s,initial(left)),
               state(r,'below left of=s'),
               state(t,'below right of=s'),
               return(at(0,-1.1))],
              [arc(s,eq,s,out,'in=30,out=0,loop','right'),
	       arc(s,gt,t,out,'bend left','right'),
               arc(s,lt,r,out,'bend right','left'),
               arc(r,gt,t,found_end,'no_update','bend angle=10,bend left'),
               arc(r,leq,r,maybe(b),'loop left'),
               arc(t,geq,t,maybe(b),'loop right'),
               arc(t,lt,r,found_end,'bend angle=15,bend left')],
              30).

seed_template(peak, s, 
              [state(s,initial(left)),
               state(r,'below left of=s'),
               state(t,'below right of=s'),
               return(at(0,-1))], 
              [arc(s,geq,s,out,'loop right'),
               arc(s,lt,r,out,'bend right','left'),
               arc(r,gt,t,found),
               arc(r,leq,r,maybe(b),'loop left'),
               arc(t,gt,t,in,'loop right'),
               arc(t,eq,t,maybe(a),'loop below'),
               arc(t,lt,r,out(a),'bend left','below,pos=0.6')],
              40).

seed_template(plain, s,
              [state(s,initial(right)),
               state(r,'below of=s'),
               state(t,at('$(r)-(5,0)$')),
               return(at(-2.2,-1.2))],
              [arc(s,leq,s,out,'in=228,out=258,loop,','below'),
               arc(s,gt,r,out,'','left,pos=0.7'),
               arc(r,gt,r,out,'loop right'),
               arc(r,eq,t,maybe(b),'bend angle=18,bend right,above'),
               arc(r,lt,s,found_end,'bend right','right=2'),
               arc(t,gt,r,out(r),'','left=2,below,sloped'),
               arc(t,eq,t,maybe(b),'loop left'),
               arc(t,lt,s,found_end,'bend left','left=2,above,sloped')],
              32).

seed_template(plateau, s,
              [state(s,initial(right)),
               state(r,'below of=s'),
               state(t,at('$(r)-(5,0)$')),
               return(at(-2.2,-1.2))], 
              [arc(s,geq,s,out,'in=228,out=258,loop,','below'),
               arc(s,lt,r,out,'','left,pos=0.7'),
               arc(r,lt,r,out,'loop right'),
               arc(r,eq,t,maybe(b),'bend angle=18,bend right,above'),
               arc(r,gt,s,found_end,'bend right','right=2'),
               arc(t,lt,r,out(r),'','left=2,below,sloped'),
               arc(t,eq,t,maybe(b),'loop left'),
               arc(t,gt,s,found_end,'bend left','left=2,above,sloped')],
              32).

seed_template(proper_plain, s, 
              [state(s,initial(right)),
               state(r,'below of=s'),
               state(t,at('$(r)-(5,0)$')),
               return(at(-2.2,-1.2))], 
              [arc(s,leq,s,out,'in=228,out=258,loop,','below'),
	       arc(s,gt,r,out,'','left,pos=0.7'),
               arc(r,gt,r,out,'loop right'),
               arc(r,eq,t,maybe(b),'bend angle=18,bend right,above'),
               arc(r,lt,s,out,'bend right','right=2'),
	       arc(t,eq,t,maybe(b),'loop left'),
               arc(t,gt,r,out(r),'','left=2,below,sloped'),
               arc(t,lt,s,found_end,'bend left','left=2,above,sloped')],
              32).

seed_template(proper_plateau, s,
              [state(s,initial(right)),
               state(r,'below of=s'),
               state(t,at('$(r)-(5,0)$')),
               return(at(-2.2,-1.2))], 
              [arc(s,geq,s,out,'in=228,out=258,loop,','below'),
               arc(s,lt,r,out,'','left,pos=0.7'),
               arc(r,lt,r,out,'loop right'),
               arc(r,eq,t,maybe(b),'bend angle=18,bend right,above'),
               arc(r,gt,s,out,'bend right','right=2'),
               arc(t,eq,t,maybe(b),'loop left'),
               arc(t,lt,r,out(r),'','left=2,below,sloped'),
	       arc(t,gt,s,found_end,'bend left','left=2,above,sloped')],
              32).

seed_template(steady, s, 
              [state(s,initial(above)),
               return(at(0,-1.5))], 
              [arc(s,neq,s,out,'loop right'),
               arc(s,eq,s,found_end,'loop left')],
              30).

seed_template(steady_sequence, s, 
              [state(s,initial(above)),
               state(r,'below of=s'),
               return(at('$(s)!0.5!(r)$'),'rotate=90')], 
              [arc(s,neq,s,out,'loop right'),
               arc(s,eq,r,found,'bend left'),
               arc(r,neq,s,out(a),'bend left'),
               arc(r,eq ,r,in,'loop right')],
              30).

seed_template(strictly_decreasing_sequence, s, 
              [state(s,initial(above)),
               state(r,'below of=s'),
               return(at('$(s)!0.5!(r)$'),'rotate=90')], 
              [arc(s,gt,r,found,'bend left'),
               arc(s,leq,s,out,'loop right'),
               arc(r,gt,r,in,'loop right'),
               arc(r,leq,s,out(a),'bend left')],
              30).

seed_template(strictly_increasing_sequence, s, 
              [state(s,initial(above)),
               state(r,'below of=s'),
               return(at('$(s)!0.5!(r)$'),'rotate=90')], 
              [arc(s,geq,s,out,'loop right'),
               arc(s,lt,r,found,'bend left'),
               arc(r,geq,s,out(a),'bend left'),
               arc(r,lt,r,in,'loop right')],
              30).

seed_template(summit, s, 
              [state(s,initial(left)),
               state(r,'right of=s'),
               state(t,'below right of=r'),
               state(u,at('$(s)!0.4!(r)-(0,4.5)$')),
               return(at('$(s)!0.4!(r)-(0,0.4)$'))],
              [arc(s,geq,s,out,'loop above'),
               arc(s,lt,r,out,'bend angle=10,bend left'),
               arc(r,lt,r,maybe(b),'loop above'),
               arc(r,gt,t,found,'bend angle=10,bend left','very near start'),
               arc(r,eq,u,maybe(b),'bend angle=10,bend left','very near end'),
               arc(t,eq,t,maybe(a),'loop above','right'),
               arc(t,gt,t,in,'loop below','near start,right'),
               arc(t,lt,r,out(a),'bend angle=10,bend left','sloped,below=2pt,near start'),
               arc(u,eq,u,maybe(b),'loop below'),
               arc(u,lt,r,maybe(b),'bend angle=10,bend left','above=2,sloped'),
               arc(u,gt,s,out(r),'bend angle=10,bend left','below=2,sloped')],
              40).

seed_template(valley, s, 
              [state(s,initial(left)),
               state(r,'below left of=s'),
               state(t,'below right of=s'),
               return(at(0,-1))], 
              [arc(s,gt,r,out,'bend right','left'),
               arc(s,leq,s,out,'loop right'),
               arc(r,geq,r,maybe(b),'loop left'),
               arc(r,lt,t,found),
               arc(t,gt,r,out(a),'bend left','below,pos=0.6'),
               arc(t,eq,t,maybe(a),'loop below'),
               arc(t,lt,t,in,'loop right')],
              40).

seed_template(zigzag, s,
	      [state(s,initial(left)),
               state(a,'below left of=s'),
               state(b,'below of=a'),
               state(c,'below of=b'),
               state(d,'below right of=s'),
               state(e,'below of=d'),
               state(f,'below of=e'),
               return(at(0,-8.51))],
              [arc(s,gt,d,out,'bend left','right'),
               arc(s,eq,s,out,'loop above'),
               arc(s,lt,a,out,'bend right','left'),
               arc(a,gt,b,maybe(b),'','sloped,below=2pt,pos=0.6'),
               arc(a,eq,s,out,no_show),
               arc(a,lt,a,out,'loop left'),
               arc(b,gt,d,out(r),'bend angle=10,bend left','sloped,above,very near end'),
               arc(b,eq,s,out(r),no_show),
               arc(b,lt,c,found,'','sloped,below=2pt,pos=0.4'),
               arc(c,gt,f,in,'draw=violet','above=2pt'),	       
               arc(c,eq,s,out(a),no_show),
               arc(c,lt,a,out(a),'bend angle=35,bend left','left'),
               arc(d,gt,d,out,'loop right'),
               arc(d,eq,s,out,no_show),
               arc(d,lt,e,maybe(b),'','sloped,below=2pt,pos=0.6'),
               arc(e,gt,f,found,'','sloped,below=2pt,pos=0.4'),
               arc(e,eq,s,out(r),no_show),
               arc(e,lt,a,out(r),'bend angle=10,bend right','sloped,above,very near end'),
               arc(f,gt,d,out(a),'bend angle=35,bend right','right'),
               arc(f,eq,s,out(a),no_show),
               arc(f,lt,c,in,'bend angle=25,bend left,draw=violet','sloped,below=2pt')],
              50).

seed_template(zigzag2, s,
	      [state(s,initial(left)),
               state(f,at('$(s)-(20mm,40mm)$')),
               state(e,at('$(f)-(0mm,55mm)$')),
               state(d,at('$(e)-(0mm,55mm)$')),
               state(a,'left of=f'),
               state(b,'left of=e'),
               state(c,'left of=d'),
               state(l,at('$(s)-(-20mm,40mm)$')),
               state(k,at('$(l)-(0mm,55mm)$')),
               state(j,at('$(k)-(0mm,55mm)$')),
               state(g,'right of=l'),
               state(h,'right of=k'),
               state(i,'right of=j'),
	       return(at(0,-6))],
              [arc(s,lt,a,out,'bend angle=10,bend right','sloped,above=2pt,pos=0.5'),
	       arc(s,gt,g,out,'bend angle=10,bend left','sloped,above=2pt,pos=0.5'),
               arc(s,eq,s,out,'loop above'),
	       arc(a,lt,f,out,'','above=2pt'),
	       arc(a,gt,b,maybe(b),'','sloped,below=2pt'),
               arc(a,eq,s,out,no_show),
               arc(b,lt,d,found,'','sloped,above=2pt,pos=0.5'),
	       arc(b,gt,c,maybe(b),'','sloped,below=2pt'),
               arc(b,eq,s,out(r),no_show),
               arc(c,lt,d,found,'','below=2pt'),
               arc(c,gt,l,out(r),'bend angle=30,bend left','sloped,above=2pt,pos=0.35'),
               arc(c,eq,s,out(r),no_show),
               arc(d,lt,e,in,'no_update','sloped,below=2pt'),
               arc(d,gt,j,in,'no_update','above=2pt'),
               arc(d,eq,s,out(a),no_show),
               arc(e,gt,j,in,'no_update','sloped,above=2pt,pos=0.1'),
               arc(e,lt,f,out(a),'','sloped,below=2pt,pos=0.2'),
               arc(e,eq,s,out(a),no_show),
               arc(f,lt,f,out,'loop above'),
	       arc(f,gt,b,maybe(b),'','sloped,above=2pt'),
               arc(f,eq,s,out,no_show),
	       arc(g,gt,l,out,'','above=2pt'),
	       arc(g,lt,h,maybe(b),'','sloped,above=2pt'),
               arc(g,eq,s,out,no_show),
               arc(h,gt,j,found,'','sloped,above=2pt,pos=0.5'),
	       arc(h,lt,i,maybe(b),'','sloped,above=2pt'),
               arc(h,eq,s,out(r),no_show),
               arc(i,gt,j,found,'','below=2pt'),
               arc(i,lt,f,out(r),'bend angle=30,bend right','sloped,above=2pt,pos=0.35'),
               arc(i,eq,s,out(r),no_show),
               arc(j,gt,k,in,'no_update','sloped,above=2pt'),
               arc(j,lt,d,in,'bend left,','below=2pt'),
               arc(j,eq,s,out(a),no_show),
               arc(k,lt,d,in,'no_update','sloped,above=2pt,pos=0.1'),
               arc(k,gt,l,out(a),'','sloped,above=2pt,pos=0.2'),
               arc(k,eq,s,out(a),no_show),
               arc(l,gt,l,out,'loop above'),
	       arc(l,lt,h,maybe(b),'','sloped,above=2pt'),
               arc(l,eq,s,out,no_show)],
              50).

% parametrized glue matrices by the feature f and the aggregation g
seed_glue_matrix(decreasing,
		 [cell(s,s,g(cf,cb))]).

seed_glue_matrix(decreasing_sequence,
		 [cell(s,s,g(cf,cb)),
		  cell(s,t,g(cf,cb)),
		  cell(t,s,g(cf,cb)),
		  cell(t,t,f(cf,f(cb,f(df,f(db,deltahat)))))]).

seed_glue_matrix(decreasing_terrace,
		 [cell(s,s,g(cf,cb)),
		  cell(s,r,g(cf,cb)),
		  cell(s,t,g(cf,cb)),
		  cell(r,s,g(cf,cb)),
		  cell(r,r,g(cf,cb)),
		  cell(r,t,f(df,f(db,delta))),
		  cell(t,s,g(cf,cb)),
		  cell(t,r,f(df,f(db,delta))),
		  cell(t,t,f(df,f(db,delta)))]).

seed_glue_matrix(gorge,
		 [cell(s,s,g(cf,cb)),
		  cell(s,r,g(cf,cb)),
		  cell(s,t,g(cf,cb)),
		  cell(s,u,g(cf,cb)),
		  cell(r,s,g(cf,cb)),
		  cell(r,r,f(df,f(db,delta))),
		  cell(r,t,f(cb,f(df,f(db,delta)))),
		  cell(r,u,g(cf,cb)),
		  cell(t,s,g(cf,cb)),
		  cell(t,r,f(cf,f(df,f(db,delta)))),
		  cell(t,t,g(cf,cb)),
		  cell(t,u,f(cf,f(df,f(db,delta)))),
		  cell(u,s,g(cf,cb)),
		  cell(u,r,g(cf,cb)),
		  cell(u,t,f(cb,f(df,f(db,delta)))),
		  cell(u,u,g(cf,cb))]).

seed_glue_matrix(increasing,
		 [cell(s,s,g(cf,cb))]).

seed_glue_matrix(increasing_sequence,
		 [cell(s,s,g(cf,cb)),
		  cell(s,t,g(cf,cb)),
		  cell(t,s,g(cf,cb)),
		  cell(t,t,f(cf,f(cb,f(df,f(db,deltahat)))))]).

seed_glue_matrix(increasing_terrace,
		 [cell(s,s,g(cf,cb)),
		  cell(s,r,g(cf,cb)),
		  cell(s,t,g(cf,cb)),
		  cell(r,s,g(cf,cb)),
		  cell(r,r,g(cf,cb)),
		  cell(r,t,f(df,f(db,delta))),
		  cell(t,s,g(cf,cb)),
		  cell(t,r,f(df,f(db,delta))),
		  cell(t,t,f(df,f(db,delta)))]).

seed_glue_matrix(peak,
		 [cell(s,s,g(cf,cb)),
		  cell(s,r,g(cf,cb)),
		  cell(s,t,g(cf,cb)),
		  cell(r,s,g(cf,cb)),
		  cell(r,r,f(df,f(db,delta))),
		  cell(r,t,f(cb,f(df,f(db,delta)))),
		  cell(t,s,g(cf,cb)),
		  cell(t,r,f(cf,f(df,f(db,delta)))),
		  cell(t,t,g(cf,cb))]).

seed_glue_matrix(plain,
		 [cell(s,s,g(cf,cb)),
		  cell(s,r,g(cf,cb)),
		  cell(s,t,g(cf,cb)),
		  cell(r,s,g(cf,cb)),
		  cell(r,r,f(df,f(db,delta))),
		  cell(r,t,f(df,f(db,delta))),
		  cell(t,s,g(cf,cb)),
		  cell(t,r,f(df,f(db,delta))),
		  cell(t,t,f(df,f(db,delta)))]).

seed_glue_matrix(plateau,
		 [cell(s,s,g(cf,cb)),
		  cell(s,r,g(cf,cb)),
		  cell(s,t,g(cf,cb)),
		  cell(r,s,g(cf,cb)),
		  cell(r,r,f(df,f(db,delta))),
		  cell(r,t,f(df,f(db,delta))),
		  cell(t,s,g(cf,cb)),
		  cell(t,r,f(df,f(db,delta))),
		  cell(t,t,f(df,f(db,delta)))]).

seed_glue_matrix(proper_plain,
		 [cell(s,s,g(cf,cb)),
		  cell(s,r,g(cf,cb)),
		  cell(s,t,g(cf,cb)),
		  cell(r,s,g(cf,cb)),
		  cell(r,r,g(cf,cb)),
		  cell(r,t,f(df,f(db,delta))),
		  cell(t,s,g(cf,cb)),
		  cell(t,r,f(df,f(db,delta))),
		  cell(t,t,f(df,f(db,delta)))]).

seed_glue_matrix(proper_plateau,
		 [cell(s,s,g(cf,cb)),
		  cell(s,r,g(cf,cb)),
		  cell(s,t,g(cf,cb)),
		  cell(r,s,g(cf,cb)),
		  cell(r,r,g(cf,cb)),
		  cell(r,t,f(df,f(db,delta))),
		  cell(t,s,g(cf,cb)),
		  cell(t,r,f(df,f(db,delta))),
		  cell(t,t,f(df,f(db,delta)))]).

seed_glue_matrix(steady,
		 [cell(s,s,g(cf,cb))]).

seed_glue_matrix(steady_sequence,
		 [cell(s,s,g(cf,cb)),
		  cell(s,r,g(cf,cb)),
		  cell(r,s,g(cf,cb)),
		  cell(r,r,f(cf,f(cb,f(df,f(db,deltahat)))))]).

seed_glue_matrix(strictly_decreasing_sequence,
		 [cell(s,s,g(cf,cb)),
		  cell(s,r,g(cf,cb)),
		  cell(r,s,g(cf,cb)),
		  cell(r,r,f(cf,f(cb,f(df,f(db,deltahat)))))]).

seed_glue_matrix(strictly_increasing_sequence,
		 [cell(s,s,g(cf,cb)),
		  cell(s,r,g(cf,cb)),
		  cell(r,s,g(cf,cb)),
		  cell(r,r,f(cf,f(cb,f(df,f(db,deltahat)))))]).

seed_glue_matrix(summit,
		 [cell(s,s,g(cf,cb)),
		  cell(s,r,g(cf,cb)),
		  cell(s,t,g(cf,cb)),
		  cell(s,u,g(cf,cb)),
		  cell(r,s,g(cf,cb)),
		  cell(r,r,f(df,f(db,delta))),
		  cell(r,t,f(cb,f(df,f(db,delta)))),
		  cell(r,u,g(cf,cb)),
		  cell(t,s,g(cf,cb)),
		  cell(t,r,f(cf,f(df,f(db,delta)))),
		  cell(t,t,g(cf,cb)),
		  cell(t,u,f(cf,f(df,f(db,delta)))),
		  cell(u,s,g(cf,cb)),
		  cell(u,r,g(cf,cb)),
		  cell(u,t,f(cb,f(df,f(db,delta)))),
		  cell(u,u,g(cf,cb))]).

seed_glue_matrix(valley,
		 [cell(s,s,g(cf,cb)),
		  cell(s,r,g(cf,cb)),
		  cell(s,t,g(cf,cb)),
		  cell(r,s,g(cf,cb)),
		  cell(r,r,f(df,f(db,delta))),
		  cell(r,t,f(cb,f(df,f(db,delta)))),
		  cell(t,s,g(cf,cb)),
		  cell(t,r,f(cf,f(df,f(db,delta)))),
		  cell(t,t,g(cf,cb))]).

seed_glue_matrix(zigzag,
                 [cell(s,s,g(cf,cb)),
		  cell(s,a,g(cf,cb)),
		  cell(s,b,g(cf,cb)),
		  cell(s,c,g(cf,cb)),
		  cell(s,d,g(cf,cb)),
		  cell(s,e,g(cf,cb)),
		  cell(s,f,g(cf,cb)),
		  cell(a,s,g(cf,cb)),
		  cell(a,a,g(cf,cb)),
		  cell(a,b,g(cf,cb)),
		  cell(a,c,f(cb,f(df,f(db,delta)))),
		  cell(a,d,g(cf,cb)),
		  cell(a,e,f(df,f(db,delta))),
		  cell(a,f,g(cf,cb)),
		  cell(b,s,g(cf,cb)),
		  cell(b,a,g(cf,cb)),
		  cell(b,b,f(df,f(db,delta))),
		  cell(b,c,g(cf,cb)),
		  cell(b,d,f(df,f(db,delta))),
		  cell(b,e,g(cf,cb)),
		  cell(b,f,f(cb,f(df,f(db,delta)))),
		  cell(c,s,g(cf,cb)),
		  cell(c,a,f(cf,f(df,f(db,delta)))),
		  cell(c,b,g(cf,cb)),
		  cell(c,c,f(cf,f(cb,f(df,f(db,delta))))),
		  cell(c,d,g(cf,cb)),
		  cell(c,e,f(cf,f(df,f(db,delta)))),
		  cell(c,f,g(cf,cb)),
		  cell(d,s,g(cf,cb)),
		  cell(d,a,g(cf,cb)),
		  cell(d,b,f(df,f(db,delta))),
		  cell(d,c,g(cf,cb)),
		  cell(d,d,g(cf,cb)),
		  cell(d,e,g(cf,cb)),
		  cell(d,f,f(cb,f(df,f(db,delta)))),
		  cell(e,s,g(cf,cb)),
		  cell(e,a,f(df,f(db,delta))),
		  cell(e,b,g(cf,cb)),
		  cell(e,c,f(cb,f(df,f(db,delta)))),
		  cell(e,d,g(cf,cb)),
		  cell(e,e,f(df,f(db,delta))),
		  cell(e,f,g(cf,cb)),
		  cell(f,s,g(cf,cb)),
		  cell(f,a,g(cf,cb)),
		  cell(f,b,f(cf,f(df,f(db,delta)))),
		  cell(f,c,g(cf,cb)),
		  cell(f,d,f(cf,f(df,f(db,delta)))),
		  cell(f,e,g(cf,cb)),
		  cell(f,f,f(cf,f(cb,f(df,f(db,delta)))))]).
