\version "2.24.2"

\header {
  title = "Pick Me Up, Love"
  composer = "—transcribed"
}

\score {
  <<
    %–– chord symbols ––
    \new ChordNames \chordmode {
      \set chordChanges = ##t
      \partial 2  % pickup
      s2       % no chord on pickup
      c2              % “Pick me” (first two beats of bar 1)
      c2              % “up, love,” (beats 3–4)
      c2              % “pick me” (beats 1–2 of bar 2)
      c2              % “up, love,” (beats 3–4)
      c4 f4           % “ev-er-” (bar 3)
      c4 f4           % “-y day.” (bar 4)
      % (then at bar 5 onward the Moderately section:)
      c4 f4 c4 f4     % one bar
      c4 f4 c4 bes4   % next bar (B♭sus2)
      c4 c4           % finish
    }

    %–– right‐hand (melody + lyrics) ––
    \new Staff \with {
      instrumentName = "Voice"
    } {
      \clef treble
      \key c \major
      \time 4/4
      \tempo 4 = 100

      \partial 2  % pick-up of two eighths
      e'8  g8       % “Pick me”
      a4            % “up,”
      g4            % “love,”
      e8  g8   a4   % “pick me up”
      g4            % “love,”
      e8  g8        % “ev-er-”
      a8 b8 a4      % “-y day.”
      %–– bar 5 onward (Moderately section)
      % rest for one bar
      r4 r4 r4 r4
      % bar 6 RH accompaniment from piano
      c'8 c8 c4 c8  c8 c8 c4 c8
      g4 g4
    }

    \addlyrics {
      Pick me up, love, pick me up, love, ev -- er -- y day.
    }

    %–– left‐hand (piano accompaniment) ––
    \new Staff \with {
      instrumentName = "Piano"
    } {
      \clef bass
      \key c \major
      \time 4/4

      \partial 2
      c,8  c,8
      f4    f4
      c,8  c,8
      f4    f4
      c,8  c,8
      bes,4 bes4
      c,4  c,4

      %–– Moderately section ––
      r4 r4 r4 r4
      <c,, f,>8 <c f>8 <c,, f,>4 <c f>8
      <c,, f,>8 <c f>8 <bes, d>4 <bes d>8
      <c,, f,>8 <c f>8
    }
  >>
  \layout { }
  \midi { }
}
