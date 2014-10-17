ECANTORIX = ../ecantorix.pl

ALL = \
      apres.wav \
      overture.wav \
      overture-osp.wav \
      entchen.wav \
      entchen-osp.wav \
      
all: $(ALL)

espeak-data:
	$(RM) -r espeak-data
	mkdir espeak-data
	cp -R /usr/share/espeak-data/* espeak-data/
	cp -R ~/espeak-data/* espeak-data/ || true
	cp extravoices/* espeak-data/voices/\!v

%.mid: %.abc
	abc2midi $< 0 -o $@

%.mmp %.ass: %.mid %.conf espeak-data
	mkdir -p cache
	$(ECANTORIX) -C $*.conf -c cache -O mmp -o $*.mmp $< | tee $*.ass

%.wav %.ass: %.mid %.conf espeak-data
	mkdir -p cache
	$(ECANTORIX) -C $*.conf -c cache -O wav -o $*.wav $< | tee $*.ass

%-xon.mid %.ass: %.mid %.conf espeak-data
	mkdir -p cache
	$(ECANTORIX) -C $*.conf -c cache -O mid --output-mid-prefix=vocals: -o $*-xon.mid $< | tee $*.ass

clean:
	$(RM) -r espeak-data cache
	$(RM) *.wav *.mid *.mmp *.ass
