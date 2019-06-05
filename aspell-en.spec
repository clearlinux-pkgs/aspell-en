#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x71C636695B147849 (dict-upload@aspell.net)
#
Name     : aspell-en
Version  : 2018.04.16.0
Release  : 10
URL      : https://mirrors.ocf.berkeley.edu/gnu/aspell/dict/en/aspell6-en-2018.04.16-0.tar.bz2
Source0  : https://mirrors.ocf.berkeley.edu/gnu/aspell/dict/en/aspell6-en-2018.04.16-0.tar.bz2
Source99 : https://mirrors.ocf.berkeley.edu/gnu/aspell/dict/en/aspell6-en-2018.04.16-0.tar.bz2.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause BSD-4-Clause HPND Public-Domain
BuildRequires : aspell
Patch1: 0001-Allow-unrecognized-options.patch

%description
GNU Aspell 0.60 English Dictionary Package
Version 2018.04.16-0
2018-04-16
Original Word List By:
Kevin Atkinson <kevina at gnu org>
Wordlist URL: http://wordlist.aspell.net/
Source Version: 2018.04.16
This word list is considered both complete and accurate.

%prep
%setup -q -n aspell6-en-2018.04.16-0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524588966
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1524588966
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/aspell-0.60/american-variant_0.alias
/usr/lib64/aspell-0.60/american-variant_1.alias
/usr/lib64/aspell-0.60/american-w_accents.alias
/usr/lib64/aspell-0.60/american-wo_accents.alias
/usr/lib64/aspell-0.60/american.alias
/usr/lib64/aspell-0.60/australian-variant_0.alias
/usr/lib64/aspell-0.60/australian-variant_1.alias
/usr/lib64/aspell-0.60/australian-w_accents.alias
/usr/lib64/aspell-0.60/australian-wo_accents.alias
/usr/lib64/aspell-0.60/australian.alias
/usr/lib64/aspell-0.60/british-ise-w_accents.alias
/usr/lib64/aspell-0.60/british-ise-wo_accents.alias
/usr/lib64/aspell-0.60/british-ise.alias
/usr/lib64/aspell-0.60/british-ize-w_accents.alias
/usr/lib64/aspell-0.60/british-ize-wo_accents.alias
/usr/lib64/aspell-0.60/british-ize.alias
/usr/lib64/aspell-0.60/british-variant_0.alias
/usr/lib64/aspell-0.60/british-variant_1.alias
/usr/lib64/aspell-0.60/british-w_accents.alias
/usr/lib64/aspell-0.60/british-wo_accents.alias
/usr/lib64/aspell-0.60/british.alias
/usr/lib64/aspell-0.60/canadian-variant_0.alias
/usr/lib64/aspell-0.60/canadian-variant_1.alias
/usr/lib64/aspell-0.60/canadian-w_accents.alias
/usr/lib64/aspell-0.60/canadian-wo_accents.alias
/usr/lib64/aspell-0.60/canadian.alias
/usr/lib64/aspell-0.60/en-common.rws
/usr/lib64/aspell-0.60/en-variant_0.multi
/usr/lib64/aspell-0.60/en-variant_0.rws
/usr/lib64/aspell-0.60/en-variant_1.multi
/usr/lib64/aspell-0.60/en-variant_1.rws
/usr/lib64/aspell-0.60/en-variant_2.multi
/usr/lib64/aspell-0.60/en-variant_2.rws
/usr/lib64/aspell-0.60/en-w_accents-only.rws
/usr/lib64/aspell-0.60/en-w_accents.multi
/usr/lib64/aspell-0.60/en-wo_accents-only.rws
/usr/lib64/aspell-0.60/en-wo_accents.multi
/usr/lib64/aspell-0.60/en.dat
/usr/lib64/aspell-0.60/en.multi
/usr/lib64/aspell-0.60/en_AU-variant_0.multi
/usr/lib64/aspell-0.60/en_AU-variant_0.rws
/usr/lib64/aspell-0.60/en_AU-variant_1.multi
/usr/lib64/aspell-0.60/en_AU-variant_1.rws
/usr/lib64/aspell-0.60/en_AU-w_accents-only.rws
/usr/lib64/aspell-0.60/en_AU-w_accents.multi
/usr/lib64/aspell-0.60/en_AU-wo_accents-only.rws
/usr/lib64/aspell-0.60/en_AU-wo_accents.multi
/usr/lib64/aspell-0.60/en_AU.multi
/usr/lib64/aspell-0.60/en_CA-variant_0.multi
/usr/lib64/aspell-0.60/en_CA-variant_0.rws
/usr/lib64/aspell-0.60/en_CA-variant_1.multi
/usr/lib64/aspell-0.60/en_CA-variant_1.rws
/usr/lib64/aspell-0.60/en_CA-w_accents-only.rws
/usr/lib64/aspell-0.60/en_CA-w_accents.multi
/usr/lib64/aspell-0.60/en_CA-wo_accents-only.rws
/usr/lib64/aspell-0.60/en_CA-wo_accents.multi
/usr/lib64/aspell-0.60/en_CA.multi
/usr/lib64/aspell-0.60/en_GB-ise-w_accents-only.rws
/usr/lib64/aspell-0.60/en_GB-ise-w_accents.multi
/usr/lib64/aspell-0.60/en_GB-ise-wo_accents-only.rws
/usr/lib64/aspell-0.60/en_GB-ise-wo_accents.multi
/usr/lib64/aspell-0.60/en_GB-ise.multi
/usr/lib64/aspell-0.60/en_GB-ize-w_accents-only.rws
/usr/lib64/aspell-0.60/en_GB-ize-w_accents.multi
/usr/lib64/aspell-0.60/en_GB-ize-wo_accents-only.rws
/usr/lib64/aspell-0.60/en_GB-ize-wo_accents.multi
/usr/lib64/aspell-0.60/en_GB-ize.multi
/usr/lib64/aspell-0.60/en_GB-variant_0.multi
/usr/lib64/aspell-0.60/en_GB-variant_0.rws
/usr/lib64/aspell-0.60/en_GB-variant_1.multi
/usr/lib64/aspell-0.60/en_GB-variant_1.rws
/usr/lib64/aspell-0.60/en_GB-w_accents.multi
/usr/lib64/aspell-0.60/en_GB-wo_accents.multi
/usr/lib64/aspell-0.60/en_GB.multi
/usr/lib64/aspell-0.60/en_US-variant_0.multi
/usr/lib64/aspell-0.60/en_US-variant_1.multi
/usr/lib64/aspell-0.60/en_US-w_accents-only.rws
/usr/lib64/aspell-0.60/en_US-w_accents.multi
/usr/lib64/aspell-0.60/en_US-wo_accents-only.rws
/usr/lib64/aspell-0.60/en_US-wo_accents.multi
/usr/lib64/aspell-0.60/en_US.multi
/usr/lib64/aspell-0.60/en_affix.dat
/usr/lib64/aspell-0.60/en_phonet.dat
/usr/lib64/aspell-0.60/english-variant_0.alias
/usr/lib64/aspell-0.60/english-variant_1.alias
/usr/lib64/aspell-0.60/english-variant_2.alias
/usr/lib64/aspell-0.60/english-w_accents.alias
/usr/lib64/aspell-0.60/english-wo_accents.alias
/usr/lib64/aspell-0.60/english.alias
