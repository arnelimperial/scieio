from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("scieio.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("products/", include("scieio.categories.urls", namespace="categories")),
    path("analytical-instruments/", include("scieio.analytical_instruments.urls", namespace="analytical_instruments")),
    path("chromatography/", include("scieio.chromatography.urls", namespace="chromatography")),
    path("brands/", include("scieio.manufacturers.urls", namespace="manufacturers")),
    path("sellers/", include("scieio.sellers.urls", namespace="sellers")),
    path("product-conditions/", include("scieio.conditions.urls", namespace="conditions")),
    path("mass-spectrometry/", include("scieio.spectrometry.urls")),
    path("spectroscopy/", include("scieio.spectroscopy.urls")),
    path("elemental-analyzers/", include("scieio.elemental_analyzers.urls")),
    path("life-sciences/", include("scieio.life_sciences.urls")),
    path("dna-synthesizers/", include("scieio.dna_synthesizers.urls")),
    path("microarray-scanners/", include("scieio.microarray.urls")),
    path("immunoassay-systems/", include("scieio.immunoassay.urls")),
    path("biotechnology/", include("scieio.biotechnology.urls")),
    path("fermenters-and-bioreactors/", include("scieio.bioreactors.urls")),
    path("dna-sequencers/", include("scieio.dna_sequencer.urls")),
    #path("bonders/", include("scieio.bonders.urls")),
    # path("disposition/", include("scieio.disposition.urls")),
    #path("viscometer-and-rheometer/", include("scieio.viscometers.urls")),
    #path("test-and-semiconductor/", include("scieio.test_semiconductor.urls")),
    #path("hardness-tester/", include("scieio.hardness.urls")),
    path("process-equipment/", include("scieio.process.urls")),
    path("food-processing-equipment/", include("scieio.food_processing.urls")),
    path("pharmaceutical-equipment/", include("scieio.pharmaceutical.urls")),
    path("water-treatment-equipment/", include("scieio.water_treatment.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
