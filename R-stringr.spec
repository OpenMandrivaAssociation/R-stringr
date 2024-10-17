%bcond_with       bootstrap
%global packname  stringr
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.6
Release:          3
Summary:          Make it easier to work with strings
Group:            Sciences/Mathematics
License:          GPL-2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-plyr 
%if %{without bootstrap}
Requires:         R-testthat 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-plyr 
%if %{without bootstrap}
BuildRequires:    R-testthat 
%endif

%description
stringr is a set of simple wrappers that make R's string functions more
consistent, simpler and easier to use.  It does this by ensuring that:
function and argument names (and positions) are consistent, all functions
deal with NA's and zero length character appropriately, and the output
data structures from each function matches the input data structures of
other functions.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/tests
