# Digital Audio
# music
- wav file is a raw uncompressed audio file
- 44.1 kHz aka CD sample rate is common, videos use 48
- wav files of 16 bit samples have signed values (-32768..32767) normalized to a range of -1 to 1 when loaded by a package
- WAV files of float will typically have a val $\in [-1, 1]$ but could be more
- careful loading and saving WAV files some may be ints, some maybe floats
- digital file (wav)
- f_s 44100 Hz
- \Delta t = 1/fs = 23us
- vals between -1, 1 split into 2^{16} bines

- q: what is actually being measured?
- a: differential pressure of the atmospheric pressure
- waves and speed of sound
    - $lambda = c/f$
    - $lambda$: wavelength in m
    - $c$: speed of wound 343m/s @ 20C
    - $f$: freq in Hz

# decibel calculations
- sound levels are measured on a log scale to model human perception
- $y_{dB} = 20 \log_{10}(y/y_{ref})$
- setting $y = 1$ we get $y_"dB" = 0$
- we refer to this conention as 0dBFS (0 dB full scale)
- if we want a signal of magnitude -12db

- q: why do we do -1 to 1?
- a: its just the normalized signal to be represented 

- decibel value is the magnitude of the signal, it cannot be negative# graph nns

- 44.1 kHz aka CD sample rate is common, videos use 48
- wav files of 16 bit samples have signed values (-32768..32767) normalized to a range of -1 to 1 when loaded by a package
- WAV files of float will typically have a val $\in [-1, 1]$ but could be more
- careful loading and saving WAV files some may be ints, some maybe floats
- digital file (wav)
- f_s 44100 Hz
- \Delta t = 1/fs = 23us
- vals between -1, 1 split into 2^{16} bines

- q: what is actually being measured?
- a: differential pressure on the atmospheric pressure
- waves and speed of sound
    - \lambda = c/f
    - \lambda: wavelength in m
    - c: speed of wound 343m/s @ 20C
    - f: freq in Hz

# decibel calculations
- sound levels are measured on a log scale to model human perception
- $y_{dB} = 20 \log_{10}(y/y_{ref})$
- setting $y = 1$ we get $y_{dB} = 0$
- we refer to this conention as 0dBFS (0 dB full scale)
- if we want a signal of magnitude -12db

- q: why do we do -1 to 1?
- a: its just the normalized signal to be represented 

- decibel value is the magnitude of the signal, it cannot be negative
## 01-22

- fourier synthesis aka additive fourier synthesis bc we add pure tones together
- some itruments (whistles) produce a pure tone, many produce multiple tones, at interger multiples of the same frequency
- when an instrument sounds at frequency f, we will see (some) integer multiples sound is harmonic if some suset of multiplees are present
- the timbre of an insturment depends on the 
- some instruments produce inharmonic collections of tones such as bells gamala

- fourier synthesis implementation:
    - by electronics (pasco electronic synth)
    - by sw (octave)
    - physical resonance
- defn: resonance: self reinforcing vibration at a specific frequency or at multiple frequencies
- here we consider harmonic resonance. the sum of integer multiples of the fundamental frequency
- for example for a note of $f_0 = 440$, we will have harmonics, $f_k=k f_0$, where $f_1 = f = 440 "Hz", f_2 = 880 "Hz" ...$
    
- conclustion:
- harmonic props
    - pattern in harmonic magnitudes
    - fundamental strength relative to harmonics
    - high relative to low freq energy (trumpet=hi, oboe=lo,marmonica=wide range-almost flat)
    - even vs odd harmonics
    - devcay rate eg.. 1/k, 1/(k^2)
    - may also have peaks/valleys in the shape, peaks/clusters of harmonics are called formants
    - pattern of harmonic phases, this is the timbre# music
dft review
- an orthonormal transformation from time samples
- `x[n]<-->X[k]`
- hartley transform only real?
- n=1..N
- k=1..N
- for real signals input, negative frequencies are determined and redundant
- typically, we use ther first n/2 entries of fft, though must exercise care doing packing, noting that for real x[n], X[-k] = conj(X[k])
- mel spectrogram, spectrogram which uses linear spacing at lower values and log spacing at higher

- normally we take n points, ddo the fft and then get n complex points
- there is also a real fft...
- the first element corresponds to the signal mean, this si the DC component
- white noise iid random samples, constant
- pink noise 1/f has some structure?
    - 1/f noise is known as a natural distribution of noise
- red noise 1/(f^2)