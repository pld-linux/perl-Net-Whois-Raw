#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	Whois-Raw
Summary:	Net::Whois::Raw - Perl extension for unparsed raw whois information
Summary(pl):	Net::Whois::Raw - rozszerzenie Perla dla nieprzetworzonych informacji whois
Name:		perl-Net-Whois-Raw
Version:	0.37
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	ed1086cbdf12199c3d6559ea3dd4557c
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

%description -l pl
Net::Whois::Raw odpytuje serwery NetworkSolutions dla domen ORG, EDU,
COM i NET. Dla innych domen najwy¿szego rzêdu (ang. Top Level Domains,
TLDs), u¿yta zostanie przestrzeñ nazw whois-servers.net
($TLD.whois-servers.net).

Ustawienie zmiennych $OMIT_MSG i $CHECK_FAIL sprawi i¿ rezultaty bêd±
porównane wzglêdem znanych wzorców. Pierwsza z nich spowoduje próbê
pominiêcia informacji o prawach, druga sprawi i¿ nast±pi próba
ustalenia czy wyszukiwanie siê nie powiod³o; je¶li tak, zwrócona
zostanie warto¶æ undef.

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
%{perl_vendorlib}/Net/Whois/Raw.pm
%{perl_vendorlib}/Net/Whois/Raw
%{_mandir}/man1/*
%{_mandir}/man3/*
