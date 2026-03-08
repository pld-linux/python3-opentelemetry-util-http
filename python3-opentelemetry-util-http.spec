#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Web util for OpenTelemetry
Summary(pl.UTF-8):	Narzędzia WWW dla OpenTelemetry
Name:		python3-opentelemetry-util-http
%define	subver	b0
%define	rel	1
Version:	0.61
Release:	0.%{subver}.%{rel}
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/opentelemetry-util-http/
Source0:	https://files.pythonhosted.org/packages/source/o/opentelemetry-util-http/opentelemetry_util_http-%{version}%{subver}.tar.gz
# Source0-md5:	4d553bca03751cffa0cef36478091254
URL:		https://pypi.org/project/opentelemetry-util-http/
BuildRequires:	python3-build
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
%if %{with tests}
BuildRequires:	python3-opentelemetry-api = 1.40.0
BuildRequires:	python3-opentelemetry-instrumentation = 1.40.0
BuildRequires:	python3-opentelemetry-semantic-conventions = 0.61
BuildRequires:	python3-wrapt >= 1
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
# not specified in pyproject, but usedf in code
Requires:	python3-opentelemetry-api = 1.40.0
Requires:	python3-opentelemetry-instrumentation = 1.40.0
Requires:	python3-opentelemetry-semantic-conventions = 0.61
Requires:	python3-wrapt >= 1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library contains generated code for the util http
defined by the OpenTelemetry specification.

%description -l pl.UTF-8
Ta biblioteka zawiera wygenerowany kod dla konwencji semantycznych
określonych przez specyfikację OpenTelemetry.

%prep
%setup -q -n opentelemetry_util_http-%{version}%{subver}

%build
%py3_build_pyproject

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m unittest discover -s tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/opentelemetry/util/http
%{py3_sitescriptdir}/opentelemetry_util_http-%{version}%{subver}.dist-info
