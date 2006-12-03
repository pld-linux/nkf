#
# Conditional build:
%bcond_without tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Network Kanji code conversion Filter
Summary(pl):	Sieciowy filtr konwertuj±cy kod Kanji
Name:		nkf
Version:	2.02
%define	fver	%(echo %{version} | tr -d .)
Release:	3
License:	BSD-like
Group:		Applications/Text
Source0:	http://www01.tcp-ip.or.jp/~furukawa/nkf_utf8/%{name}%{fver}.tar.gz
# Source0-md5:	5157b91879471b450997f4eec5af62e6
URL:		http://www01.tcp-ip.or.jp/~furukawa/nkf_utf8/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nkf is a yet another kanji code converter among networks, hosts and
terminals. It converts input kanji code to designated kanji code such
as 7-bit JIS, MS-kanji (shifted-JIS), utf-8 or EUC. One of the most
unique facicility of nkf is the guess of the input kanji code. It
currently recognizes 7-bit JIS, MS-kanji (shifted-JIS), utf-8 and EUC.
So users needn't the input kanji code specification.

%description -l pl
nkf to jeszcze jeden konwerter kodu kanji pomiêdzy sieciami, hostami i
terminalami. Konwertuje wej¶cie w kodzie kanji do konkretnego kodu
kanji, takiego jak 7-bitowy JIS, MS-kanji (przesuniêty JIS), utf-8 lub
EUC. Jednym z unikalnych udogodnieñ nkf jest to, ¿e rozpoznaje
wej¶ciowy kod kanji. Aktualnie rozpoznaje 7-bitowy JIS, MS-kanji
(przesuniêty JIS), utf-8 i EUC. Dziêki temu u¿ytkownicy nie musz± znaæ
specyfikacji wej¶ciowego kodu kanji.

%package -n perl-NKF
Summary:	NKF - Perl extension for Network Kanji Filter
Summary(pl):	NKF - rozszerzenie Perla dla sieciowy filtra Kanji
Group:		Development/Languages/Perl

%description -n perl-NKF
This is a Perl Extension version of nkf (Network Kanji Filter). It
converts the last argument and return converted result. Conversion
details are specified by flags before the last argument.

%description -n perl-NKF -l pl
To jest nkf (Network Kanji Filter - sieciowego filtra kanji) jako
rozszerzenie Perla. Konwertuje tekst podany jako ostatni argument i
zwraca wynik konwersji. Szczegó³y konwersji podaje siê przy pomocy
flag przed ostatnim argumentem.

%prep
%setup -q -n %{name}%{fver}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%{?with_tests:%{__make} test}

cd NKF.mod
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_mandir}/ja/man1}

%{__make} -C NKF.mod install \
	DESTDIR=$RPM_BUILD_ROOT

install nkf $RPM_BUILD_ROOT%{_bindir}
install nkf.1 $RPM_BUILD_ROOT%{_mandir}/man1
install nkf.1j $RPM_BUILD_ROOT%{_mandir}/ja/man1/nkf.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nkf
%{_mandir}/man1/nkf.1*
%{_mandir}/ja/man1/nkf.1*

%files -n perl-NKF
%defattr(644,root,root,755)
%doc NKF.mod/{Changes,README}
%{perl_vendorarch}/NKF.pm
%dir %{perl_vendorarch}/auto/NKF
%{perl_vendorarch}/auto/NKF/NKF.bs
%attr(755,root,root) %{perl_vendorarch}/auto/NKF/NKF.so
%{_mandir}/man3/*
