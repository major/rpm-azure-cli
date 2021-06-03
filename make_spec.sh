#!/bin/bash

PKG_NAME=$1
PKG_VER=$2

SUMMARY=$(curl -s https://pypi.org/pypi/${PKG_NAME}/json | jq -r .info.summary)

PKG_NAME_SLASHED=$(echo $PKG_NAME | tr '-' '/')
PKG_NAME_UNDERSCORED=$(echo $PKG_NAME | tr '-' '_')

if [ -f specs/python-${PKG_NAME}.spec ]; then
    echo "Spec file already exists."
    exit 1
fi

tee specs/python-${PKG_NAME}.spec > /dev/null << EOF


%global         srcname     ${PKG_NAME}

Name:           python-%{srcname}
Version:        ${PKG_VER}
Release:        1%{?dist}
Summary:        ${SUMMARY}
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}

BuildArch:      noarch

BuildRequires:  python3-devel

Obsoletes:      python3-azure-sdk < 5.0.1

%global _description %{expand:
${SUMMARY}}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{srcname}
%{python3_sitelib}/${PKG_NAME_SLASHED}
%{python3_sitelib}/${PKG_NAME_UNDERSCORED}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue Jun 01 2021 Major Hayden <major@mhtx.net> - ${PKG_VER}-1
- First package.
EOF

code specs/python-${PKG_NAME}.spec
./build.sh specs/python-${PKG_NAME}.spec
