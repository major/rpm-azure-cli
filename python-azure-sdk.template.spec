# Enable Python dependency generation
%{?python_enable_dependency_generator}

# Missing dependencies for tests
%bcond_with check

Name:           python-azure
Version:        20210527
Release:        1%{?dist}

Summary:        Azure SDK for Python
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
{% for package in packages -%}
{% set source_label = "Source" + ((loop.index - 1) | string) + ":" -%}
{{ source_label.ljust(16) }}%{pypi_source {{ package.name }} {{ package.version }} {{ package.extension }}}
{% endfor %}

BuildArch:      noarch

Obsoletes:      python-azure-sdk == 5.0.0-4

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

BuildRequires:  tree

%if %{with check}
# DOOT
%endif

%description
Azure SDK for Python

{% for package in packages %}
%package {{ package.short_name }}
Version: {{ package.version}}
Summary: {{ package.summary}}

%description {{ package.short_name }}
{{ package.summary}}
{% endfor %}

%prep
# Create the base directory but skip any extractions for now.
%autosetup -n %{name}-%{version} -c -T
{% for package in packages -%}
# Extract {{ package.name }} {{ package.version }}
%autosetup -n %{name}-%{version} -D -T -a {{ loop.index - 1 }}
{% endfor %}
tree -d

%build
# Set the directory where we collect the wheels during each step of the loop.
BASE_WHEELDIR=$(pwd)/pyproject-wheeldir
mkdir -vp $BASE_WHEELDIR

# Get a list of python projects that we've extracted.
PYTHON_PROJECTS=$(find . -name setup.py -maxdepth 2)

# Loop over each project, build the wheel, and move the wheel into the correct
# place.
for PYTHON_PROJECT in $PYTHON_PROJECTS; do
    pushd $(dirname $PYTHON_PROJECT)
        %pyproject_wheel
        mv pyproject-wheeldir/* $BASE_WHEELDIR
    popd
done

%install
%pyproject_install

%if %{with check}
%check
PYTHON_PROJECTS=$(find . -name setup.py -maxdepth 2)
for PYTHON_PROJECT in $PYTHON_PROJECTS; do
    pushd $(dirname $PYTHON_PROJECT)
        %pytest
    popd
done
%endif

{% for package in packages %}
%files {{ package.short_name }}
{% for file_type, file_path in package.files.items() -%}
# Packaging {{ file_type }}
{{ file_path }}
{% endfor %}
{% endfor %}

%changelog
* Thu May 27 2021 Major Hayden - 20210527-1
- First package.
