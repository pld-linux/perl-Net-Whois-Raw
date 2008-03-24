#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Whois-Raw
Summary:	Net::Whois::Raw - Perl extension for unparsed raw whois information
Summary(pl.UTF-8):	Net::Whois::Raw - rozszerzenie Perla dla nieprzetworzonych informacji whois
Name:		perl-Net-Whois-Raw
Version:	0.43
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	93f2d2a340ccca12effb0385db5d05d6
URL:		http://search.cpan.org/dist/Net-Whois-Raw/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(IO::Socket) >= 1
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Whois::Raw queries NetworkSolutions and follows the Registrar:
answer for ORG, EDU, COM and NET domains. For other TLDs it uses the
whois-servers.net namespace. ($TLD.whois-servers.net).

Setting the variables $OMIT_MSG and $CHECK_FAIL will match the results
against a set of known patterns. The first flag will try to omit the
copyright message/disclaimer, the second will attempt to determine if
the search failed and return undef in such a case.

%description -l pl.UTF-8
Net::Whois::Raw odpytuje serwery NetworkSolutions dla domen ORG, EDU,
COM i NET. Dla innych domen najwyższego rzędu (ang. Top Level Domains,
TLDs), użyta zostanie przestrzeń nazw whois-servers.net
($TLD.whois-servers.net).

Ustawienie zmiennych $OMIT_MSG i $CHECK_FAIL sprawi iż rezultaty będą
porównane względem znanych wzorców. Pierwsza z nich spowoduje próbę
pominięcia informacji o prawach, druga sprawi iż nastąpi próba
ustalenia czy wyszukiwanie się nie powiodło; jeśli tak, zwrócona
zostanie wartość undef.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/Net/Whois
%{perl_vendorlib}/Net/Whois/Raw.pm
%{perl_vendorlib}/Net/Whois/Raw
%{_mandir}/man1/*
%{_mandir}/man3/*
